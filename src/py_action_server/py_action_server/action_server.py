import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from rclpy.duration import Duration
from test_action.action import Test
from geometry_msgs.msg import Twist, PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
import time


class TestActionServer(Node):
    navigator: BasicNavigator = None

    def __init__(self, navigator):
        super().__init__('test_action_server')
        self._action_server = ActionServer(
            self,
            Test,
            'my_action',
            self.execute_callback)
        self.publisher_ = self.create_publisher(PoseStamped, '/cmd_vel', 10)
        self.navigator = navigator

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        ix, iy, iz, iw = self.get_coords_from_pos(self.navigator.initial_pose)
        # Current action has list: [x,y,z,w]
        x, y, z, w = goal_handle.request.pose
        msg = PoseStamped()
        msg.header.frame_id = 'map'
        msg.header.stamp = self.navigator.get_clock().now().to_msg()
        msg.pose.position.x = x
        msg.pose.position.y = y
        msg.pose.orientation.z = z
        msg.pose.orientation.w = w

        feedback_msg = Test.Feedback()
        feedback_msg.feedback = "Robot moving to new location..."

        self.navigator.goToPose(msg)

        i = 0
        while not self.navigator.isNavComplete():
            i += 1
            feedback = self.navigator.getFeedback()
            if feedback and i % 5 == 0:
                feedback_string = f'timestep: {i % 5} - Estimated time of arrival from [{ix},{iy},{iz},{iw}] at [{x},{y},{z},{w}]' + ' for worker: ' + '{0:.0f}'.format(
                    Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9) + ' seconds.'
                print(feedback_string)

                feedback_msg.feedback = feedback_string
                goal_handle.publish_feedback(feedback_msg)

        goal_handle.succeed()

        print('I am done')
        # msg.linear.x = 0.0
        # self.publisher_.publish(msg)

        result = Test.Result()
        result.status = f"Finished action server. Moved to position [{x},{y},{z},{w}]"
        return result

    @staticmethod
    def get_coords_from_pos(pos: PoseStamped):
        return pos.pose.position.x, pos.pose.position.y, pos.pose.orientation.z, pos.pose.orientation.w


def main(args=None):
    rclpy.init(args=args)
    navigator = BasicNavigator()
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = 3.45
    initial_pose.pose.position.y = 2.15
    initial_pose.pose.orientation.z = 1.0
    initial_pose.pose.orientation.w = 0.0
    navigator.setInitialPose(initial_pose)

    # Wait for navigation to fully activate, since autostarting nav2
    navigator.waitUntilNav2Active()

    test_action_server = TestActionServer(navigator)

    rclpy.spin(test_action_server)


if __name__ == '__main__':
    main()
