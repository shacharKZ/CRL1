from selectors import EpollSelector
import rclpy
from rclpy.node import Node
from multi_burger_interfaces.srv import Position
from geometry_msgs.msg import Twist
from gazebo_msgs.srv import GetEntityState
from time import sleep

import numpy as np
from math import pi

from crl_executer.transformations import euler_from_quaternion, yaw_from_coordinates

LINEAR_VELOCITY = 0.33  # originally 0.1  # m/s
ANGULAR_VELOCITY = pi / 10  # originally was pi / 10  # rad/s
EPSILON = 1e-3  # originally 1e-3
POLL_RATE = (1e-4)/2  # originally 1e-4# sec
POLL_RATE_FORWARD = 0.002  # ours. still in test
# DIST_EPSILON = 1e-3
# STACK_EPSILON = 1e-30

class PositionTracker(Node):
    def __init__(self, node_name: str):
        super().__init__(node_name)
        self.client = self.create_client(GetEntityState, '/get_entity_state')

        while not self.client.wait_for_service(0.5):
            self.get_logger().info('Waiting for service.')

        self.req = GetEntityState.Request()

    def get_pose(self, name):
        self.req.name = name
        self.future = self.client.call_async(self.req)


class PositionService(Node):
    def __init__(self, node_name: str) -> None:
        super().__init__(node_name)
        self.times_called = 0
        self.name = node_name

        # Position request client from gazebo
        self.position_client = PositionTracker('position_tracker')

        # Position manipulation service
        self.service = self.create_service(Position, self.get_name() + '_service', self.service_callback)
        self.pub = self.create_publisher(Twist, f'{self.name}/cmd_vel', 0)

    def get_position(self, name):
        self.position_client.get_pose(name)
        while rclpy.ok():
            rclpy.spin_once(self.position_client)
            if self.position_client.future.done():
                response: GetEntityState.Response = self.position_client.future.result()
                x = response.state.pose.position.x
                y = response.state.pose.position.y
                _, _, yaw = euler_from_quaternion(response.state.pose.orientation)

                break

        return x, y, yaw

    def service_callback(self, request, response):
        self.times_called += 1
        self.get_logger().info(f'.')
        self.get_logger().info(f'Position service for {self.name} called {self.times_called} times. '
                               f'Service got {request}')

        print("")
        if request.action == 0:
            x, y, yaw = self.to_yaw(request.x, request.y)
        elif request.action == 1:
            x, y, yaw = self.drive_closest_to_point(request.x, request.y)
        else:
            self.stop()

        response.x = x
        response.y = y
        response.yaw = yaw * 180 / pi
        self.get_logger().info(f'x: {x}, y: {y}, yaw: {yaw}')

        return response

    def to_yaw(self, x_target, y_target):
        x, y, yaw = self.get_position(self.name)
        yaw_target = yaw_from_coordinates(x_target - x, y_target - y)
        if abs(yaw - yaw_target) < EPSILON:
            return x, y, yaw

        turn = self.turn_right
        delta = (yaw - yaw_target) % (2 * pi)
        if delta >= pi:
            turn = self.turn_left
        turn()
        while (abs(yaw - yaw_target) > EPSILON) or \
                (abs(yaw % (2 * pi) - yaw_target % (2 * pi)) > EPSILON):
            sleep(POLL_RATE)
            x, y, yaw = self.get_position(self.name)

        self.stop()

        return x, y, yaw

    def drive_closest_to_point(self, x_target, y_target):

        x, y, yaw = self.get_position(self.name)
        print(f'{self.name}:)c) i think i am at x,y={x},{y}')
        drive = self.drive_forward

        # yaw_target = yaw_from_coordinates(x_target - x, y_target - y)  # TODO walking backward not supported yet
        # delta = abs(yaw - yaw_target)
        # if delta > abs(delta - np.pi):
        #     # print(f'{self.name}:)c) WTF')
        #     drive = self.drive_backward

        def l2(x_target, y_target, x_curr, y_curr):
            return np.linalg.norm([x_target - x_curr, y_target - y_curr], 2)

        def find_range(x_target, y_target):
            x, y, yaw = self.get_position(self.name)
            return l2(x_target, y_target, x, y)

        r_curr = find_range(x_target, y_target)
        drive()

        r_prev = float('inf')
        counter = 0
        # while r <= r_curr + EPSILON ** 2:  # original role
        while r_curr > EPSILON:
            sleep(5 * POLL_RATE_FORWARD)
            r_prev = r_curr
            r_curr = find_range(x_target, y_target)
            if counter < 50:
                counter += 1
            elif r_prev < r_curr - (EPSILON ** 2):
                print(f'{self.name}> stop walking according to \"STACK\" role!')
                break

        self.stop()
        # print(f'{self.name}:)f): just after stop to drive. counter was {counter}.  r_curr={r_curr}, r_prev={r_prev} ')

        return self.get_position(self.name)

    def drive_forward(self):
        forward = Twist()
        forward.linear.x = LINEAR_VELOCITY
        self.pub.publish(forward)

    def drive_backward(self):
        backward = Twist()
        backward.linear.x = -LINEAR_VELOCITY
        self.pub.publish(backward)

    def turn_right(self):
        right = Twist()
        right.angular.z = -ANGULAR_VELOCITY
        self.pub.publish(right)

    def turn_left(self):
        left = Twist()
        left.angular.z = ANGULAR_VELOCITY
        self.pub.publish(left)

    def stop(self):
        self.pub.publish(Twist())


def main():
    import sys

    print(sys.argv)
    name = sys.argv[1]
    rclpy.init()
    service = PositionService(name)
    rclpy.spin(service)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
