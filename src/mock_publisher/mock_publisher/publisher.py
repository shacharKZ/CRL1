import time
import random

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Quaternion
from goal_status_interface.msg import GoalStatus
from robot_status_interface.msg import RobotStatus
from robot_path_assignment_interface.msg import RobotPathAssignment, RobotPathAssignmentPlan
from mock_publisher.txt_to_plan import parse_txt_to_plan

PLAN_TOPIC = '/plan'
PATH_TO_PLAN = './plans_to_run/plan2.txt'
SCENE_NAME = None  # TODO


class MockPublisher(Node):
    msg_publisher = None

    def __init__(self):
        super().__init__('MockPublisher')
        self.msg_publisher = self.create_publisher(RobotPathAssignmentPlan, PLAN_TOPIC, 10)
        self.publish_mock_message_to_topic()

    def publish_mock_message_to_topic(self):
        full_message = RobotPathAssignmentPlan()
        full_plan = parse_txt_to_plan(plan_path=PATH_TO_PLAN)
        # TODO set up map/scene
        for robot_entity in full_plan:
            robot_plan = full_plan[robot_entity]
            self.get_logger().info(f'plan for robot={robot_entity} is {robot_plan}')
            single_assignment = RobotPathAssignment()
            single_assignment.target_robot_id = robot_entity
            for single_task in robot_plan:
                x = single_task[0]
                y = single_task[1]
                task_type = single_task[2]  # TODO
                custom_msg = single_task[3]  # TODO
                single_assignment.path.append(self.construct_pose_stamped(x, y, 0.1))
            single_assignment.task = 'STARfutureT'  # TODO
            full_message.plan.append(single_assignment)
        self.msg_publisher.publish(full_message)
        #
        # time.sleep(3)
        # full_message = RobotPathAssignmentPlan()
        # message = RobotPathAssignment()
        # message.target_robot_id = 1
        # message.task = 'STOP'
        # full_message.plan.append(message)
        # message1 = RobotPathAssignment()
        # message1.target_robot_id = 3
        # message1.task = 'STOP'
        # full_message.plan.append(message1)
        # self.msg_publisher.publish(full_message)


    def publish_mock_message_to_topic0(self):
        self.get_logger().info('BP1')
        message = RobotPathAssignmentPlan()
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
        # self.msg_publisher.publish(message0)
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
        # self.msg_publisher.publish(message1)
        self.get_logger().info('BP3')
        message.plan = [message0, message1]
        self.msg_publisher.publish(message)

        time.sleep(2)

        message2 = RobotPathAssignment()
        message2.target_robot_id = 2
        message2.path.append(self.construct_pose_stamped(1.0, 0.3, 0.1))
        message2.path.append(self.construct_pose_stamped(1.0, 0.8, 0.1))
        message2.path.append(self.construct_pose_stamped(1.5, 0.8, 0.1))
        message2.path.append(self.construct_pose_stamped(1.5, 0.3, 0.1))
        message2.task = 'START'
        # self.msg_publisher.publish(message2)
        self.get_logger().info('BP4')
        message.plan = [message2]
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
