import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Quaternion
from goal_status_interface.msg import GoalStatus
from robot_status_interface.msg import RobotStatus
from robot_path_assignment_interface.msg import RobotPathAssignment, RobotPathAssignmentPlan
from mock_publisher.txt_to_plan import parse_txt_to_plan
import argparse

PLAN_TOPIC = '/plan'
# PATH_TO_PLAN = './plans_to_run/test0.txt'
DEFAULT_PLAN = './plans_to_run/turtlebot3_dqn_stage2_s2.txt'
DEFAULT_WORLD = None  # TODO
QUEUE_SIZE = 30  # uses also as a bottleneck for the number of robots in scene (QUEUE_SIZE-2)


class MockPublisher(Node):
    msg_publisher = None

    def __init__(self, path_to_plan=None, map_to_load=None):
        super().__init__('MockPublisher')
        self.msg_publisher = self.create_publisher(RobotPathAssignmentPlan, PLAN_TOPIC, QUEUE_SIZE)
        self.path_to_plan = path_to_plan if path_to_plan is not None else DEFAULT_PLAN
        self.map_to_load = map_to_load if map_to_load is not None else DEFAULT_WORLD  # TODO
        self.publish_mock_message_to_topic()

    def publish_mock_message_to_topic(self):
        full_message = RobotPathAssignmentPlan()
        full_plan = parse_txt_to_plan(plan_path=self.path_to_plan)
        # TODO set up map/scene
        for robot_entity in full_plan:
            robot_plan = full_plan[robot_entity]
            self.get_logger().info(f'plan for robot={robot_entity} is {robot_plan}')
            single_assignment = RobotPathAssignment()
            single_assignment.target_robot_id = robot_entity
            for single_task in robot_plan:
                x = single_task[0]
                y = single_task[1]
                goal_msg = single_task[2]
                single_assignment.path.append(self.construct_pose_stamped(x, y, 0.1))
                single_assignment.goal_message.append(goal_msg)
            single_assignment.task = 'START'
            full_message.plan.append(single_assignment)
        self.msg_publisher.publish(full_message)

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
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--world_map", help="The name of world (map) for Gazebo",
    #                     type=str, default=None)
    # parser.add_argument("--plan", help="Path to plan for the scene",
    #                     type=str, default=None)
    # args2 = parser.parse_args()
    # node = MockPublisher(map_to_load=args2.world_map, path_to_plan=args2.plan)
    node = MockPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
