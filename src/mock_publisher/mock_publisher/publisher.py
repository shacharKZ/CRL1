import time
import random

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Quaternion
from goal_status_interface.msg import GoalStatus
from robot_status_interface.msg import RobotStatus
from robot_path_assignment_interface.msg import RobotPathAssignment


class MockPublisher(Node):
    msg_publisher = None

    def __init__(self):
        super().__init__('MockPublisher')
        self.msg_publisher = self.create_publisher(RobotPathAssignment, '/MAPF_PLAN', 10)
        # self.publish_mock_message_to_topic()
        timer_period = 1
        # self.timer = self.create_timer(timer_period, self.publish_mock_message_to_topic)
        self.publish_mock_message_to_topic0()
        # self.publish_random_message_to_topic()
        # self.publish_mock_message_to_topic()
        # self.publish_mock_message_to_topic1()

    def publish_random_message_to_topic(self):
        message = RobotPathAssignment()
        message.target_robot_id = random.randint(0, 1)
        target = self.get_rand_float(random.randint(0, 3))
        message.path.append(self.construct_pose_stamped(target, 0.0, 0.1))
        # time.sleep(1)
        # message.path.append(self.construct_pose_stamped(-1.0, 0.0, 0.1))
        # # time.sleep(1)
        # message.path.append(self.construct_pose_stamped(1.0, 1.0, 0.1))
        # # time.sleep(1)
        # message.path.append(self.construct_pose_stamped(0.0, 1.0, 0.1))
        # # time.sleep(1)
        # message.path.append(self.construct_pose_stamped(0.0, 0.0, 0.1))
        message.task = 'START'

        self.msg_publisher.publish(message)

    def get_rand_float(self, seed):
        if seed == 0:
            return 0.0
        elif seed == 1:
            return 0.5
        elif seed == 2:
            return 1.0
        elif seed == 3:
            return 1.5

    def publish_mock_message_to_topic0(self):
        self.get_logger().info('BP1')
        message0 = RobotPathAssignment()
        message0.target_robot_id = 0
        message0.path.append(self.construct_pose_stamped(0.0, 0.0, 0.1))
        message0.path.append(self.construct_pose_stamped(0.0, -0.5, 0.1))
        message0.path.append(self.construct_pose_stamped(0.5, -0.5, 0.1))
        message0.path.append(self.construct_pose_stamped(0.5, 0.0, 0.1))
        # message0.path.append(self.construct_pose_stamped(-1.0, -1.0, 0.1))
        # message0.path.append(self.construct_pose_stamped(0.0, -1.0, 0.1))
        # message0.path.append(self.construct_pose_stamped(0.0, 0.0, 0.1))
        message0.task = 'START'
        self.msg_publisher.publish(message0)
        self.get_logger().info('BP2')

        message1 = RobotPathAssignment()
        message1.target_robot_id = 1
        message1.path.append(self.construct_pose_stamped(0.0, 0.3, 0.1))
        message1.path.append(self.construct_pose_stamped(0.0, 0.8, 0.1))
        message1.path.append(self.construct_pose_stamped(0.5, 0.8, 0.1))
        message1.path.append(self.construct_pose_stamped(0.5, 0.3, 0.1))
        # message1.path.append(self.construct_pose_stamped(0.0, 0.0, 0.1))
        # message1.path.append(self.construct_pose_stamped(0.0, 1.0, 0.1))
        # message1.path.append(self.construct_pose_stamped(1.0, 1.0, 0.1))
        # message1.path.append(self.construct_pose_stamped(0.0, 1.0, 0.1))
        # message1.path.append(self.construct_pose_stamped(1.0, 1.0, 0.1))
        # message1.path.append(self.construct_pose_stamped(1.0, -1.0, 0.1))
        # message1.path.append(self.construct_pose_stamped(1.0, 0.0, 0.1))

        message1.task = 'START'
        self.msg_publisher.publish(message1)
        self.get_logger().info('BP3')

        time.sleep(2)

        message2 = RobotPathAssignment()
        message2.target_robot_id = 2
        message2.path.append(self.construct_pose_stamped(1.0, 0.3, 0.1))
        message2.path.append(self.construct_pose_stamped(1.0, 0.8, 0.1))
        message2.path.append(self.construct_pose_stamped(1.5, 0.8, 0.1))
        message2.path.append(self.construct_pose_stamped(1.5, 0.3, 0.1))
        message2.task = 'START'
        self.msg_publisher.publish(message2)
        self.get_logger().info('BP4')

    def publish_mock_message_to_topic(self):
        message = RobotPathAssignment()
        message.target_robot_id = 0
        message.path.append(self.construct_pose_stamped(0.0, 0.0, 0.1))
        # time.sleep(1)
        message.path.append(self.construct_pose_stamped(-1.0, 0.0, 0.1))
        # time.sleep(1)
        message.path.append(self.construct_pose_stamped(1.0, 1.0, 0.1))
        # time.sleep(1)
        message.path.append(self.construct_pose_stamped(0.0, 1.0, 0.1))
        # time.sleep(1)
        message.path.append(self.construct_pose_stamped(0.0, 0.0, 0.1))
        message.task = 'START'

        self.msg_publisher.publish(message)

    def publish_mock_message_to_topic1(self):
        message = RobotPathAssignment()
        message.target_robot_id = 1
        message.path.append(self.construct_pose_stamped(-1.0, 2.0, 0.1))
        time.sleep(1)
        message.path.append(self.construct_pose_stamped(-2.0, 2.0, 0.1))
        message.task = 'START'

        self.msg_publisher.publish(message)

    def construct_pose_stamped(self, px, py, pz):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()  # TODO try to look into that
        pose.pose.position.x = px
        pose.pose.position.y = py
        pose.pose.position.z = pz
        pose.pose.orientation.x = 1.0
        pose.pose.orientation.y = 1.0
        pose.pose.orientation.z = 1.0
        pose.pose.orientation.w = 1.0

        return pose


def main(args=None):
    rclpy.init(args=args)
    node = MockPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
