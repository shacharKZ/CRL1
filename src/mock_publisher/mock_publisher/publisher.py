import time

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
        self.timer = self.create_timer(timer_period, self.publish_mock_message_to_topic)

    def publish_mock_message_to_topic(self):
        message = RobotPathAssignment()
        message.target_robot_id = 0
        message.path.append(self.construct_pose_stamped(-2.0,-0.5,0.1))
        time.sleep(1)
        message.path.append(self.construct_pose_stamped(-2.5, -0.5, 0.1))
        message.task = 'START'

        self.msg_publisher.publish(message)


    def construct_pose_stamped(self, px, py, pz ):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()
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
