import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from test_action.action import Test
from geometry_msgs.msg import Twist
import time


class TestActionServer(Node):

    def __init__(self):
        super().__init__('test_action_server')
        self._action_server = ActionServer(
            self,
            Test,
            'test',
            self.execute_callback)
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        msg = Twist()
        msg.linear.x = 0.5

        for i in range(1, goal_handle.request.secs):
            self.publisher_.publish(msg)
            time.sleep(1)

        goal_handle.succeed()

        msg.linear.x = 0.0
        self.publisher_.publish(msg)

        result = Test.Result()
        result.status = "Finished action server. Moved during %d seconds" % goal_handle.request.secs
        return result


def main(args=None):
    rclpy.init(args=args)

    test_action_server = TestActionServer()

    rclpy.spin(test_action_server)


if __name__ == '__main__':
    main()