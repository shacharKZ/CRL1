import subprocess
from typing import List

import rclpy
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Pose, Twist
from gazebo_msgs.srv import GetEntityState
from goal_status_interface.msg import GoalStatus
from robot_status_interface.msg import RobotStatus
from robot_path_assignment_interface.msg import RobotPathAssignment, RobotPathAssignmentPlan
from crl_executer.path_client import PathClient
from crl_executer.position_service import PositionTracker

PLAN_TOPIC = '/plan'
INTERNAL_PLAN_TOPIC = '/planForwarder'
ROBOT_STATUS_TOPIC = '/robotStatus'
GOAL_STATUS_TOPIC = '/goalStatus'

BASE_ROBOT_TOPIC = '/robot/'

ROBOT_CACHE = {}
TIMER_PERIOD = 5


class Executer(Node):
    def __init__(self):
        super().__init__('Executer')
        self.subscribe_to_mapf_plan_topic()
        self.expose_robot_status_topic()
        self.expose_goal_status_topic()
        self.robot_status_timer = self.create_timer(TIMER_PERIOD, self.publish_robot_status)
        self.goal_status_timer = self.create_timer(TIMER_PERIOD, self.publish_goal_status)
        self.executer_tracker = PositionTracker('executer_tracker')

    def subscribe_to_mapf_plan_topic(self):
        single_robot_plan_sender_cb_group = ReentrantCallbackGroup()
        self.plan_input_topic = self.create_subscription(RobotPathAssignmentPlan, PLAN_TOPIC, self.handle_plan,
                                                         10)
        self.internal_plan_topic = self.create_publisher(RobotPathAssignment, INTERNAL_PLAN_TOPIC, 10)
        self.internal_plan_topic_handler = self.create_subscription(RobotPathAssignment, INTERNAL_PLAN_TOPIC,
                                                                    self.send_plan_to_robot, 10,
                                                                    callback_group=single_robot_plan_sender_cb_group)

    def expose_robot_status_topic(self):
        self.robot_status_topic = self.create_publisher(RobotStatus, ROBOT_STATUS_TOPIC, 10)

    def expose_goal_status_topic(self):
        self.goal_status_topic = self.create_publisher(GoalStatus, GOAL_STATUS_TOPIC, 10)

    def publish_robot_status(self):
        # Query all robot locations and send them over the topic
        self.get_logger().info('Publishing all robot status')
        for robot_id in ROBOT_CACHE.keys():
            position = self._get_position_by_name(f"robot{robot_id}")
            message = RobotStatus()
            message.robot_id = robot_id
            message.current_location = self._construct_pose_stamped(position)
            self.get_logger().info(f'Publishing status of robot {robot_id}')
            self.robot_status_topic.publish(message)

    def publish_goal_status(self):
        # Query all goal locations and send them over the topic
        pass

    # TODO: need to decide how to publish messages from both of these events, the format might be differnet, maybe we want to
    # publish from gazebo to virtual robots only, and the same from optiTrack to physical?
    def get_robot_status_from_gazebo(self):
        # TODO: how?
        # In here we will subscribe to gazebo somehow, and upon receiving events, a callback
        # will be issued that will publish the RobotStatus
        pass

    def get_robot_status_from_opti_track(self):
        # TODO: how?
        # In here we will subscribe to optiTrack somehow, and upon receiving events, a callback
        # will be issued that will publish the RobotStatus
        pass

    def handle_plan(self, msg):
        self.get_logger().info('Received a plan!')
        robot_assignments: List[RobotPathAssignment] = msg.plan
        for assignment in robot_assignments:
            self.internal_plan_topic.publish(assignment)

    def send_plan_to_robot(self, msg):
        # Assumptions
        # 1. The first task assignment for a robot must be START
        # 2. The first pose stamped in the first task assignment is the initial location of the robot
        target_robot_id = msg.target_robot_id
        self.get_logger().warn(f'Received task for robot {target_robot_id}')
        task = msg.task
        if task == 'STOP':
            self.get_logger().warn('Received STOP!')
            # Stop robot immediately
            pass
        elif task == 'START':
            self.get_logger().warn('Received START!')
            for path_target in msg.path:
                if target_robot_id not in ROBOT_CACHE:
                    # This is the first message about this robot, and the robot has no initial position, so the first pose stamped is the robots' initial position
                    self._save_robot_initial_position(target_robot_id, path_target)
                    self._spawn_burger_bot_and_service(target_robot_id, path_target)
                else:
                    self._send_next_point_to_robot(target_robot_id, path_target)
            # This is another command in the robot's lifecycle, need to send him the command using the client
            # Tell robot to stop performing current tasks and begin a new path
            # command = self._get_twist_from_pose_pair(msg.path[0], msg.path[1])
            # self._send_twist_message_base(command)
            # self._send_twist_message_base(0)
            # self._send_twist_message(0)
            # self._send_twist_message_1(1)
        elif task == 'EXTEND':
            self.get_logger().warn('Received EXTEND!')
            # Tell the robot to continue with these added assignments after it is done with current tasks
            pass

    def _send_twist_message_base(self, robot_id):
        self.get_logger().warn('Sending twist message!')
        cmd_vel_pub = self.create_publisher(Twist, f'/cmd_vel', 10)
        twist_msg = Twist()
        twist_msg.linear.x = 0.1
        twist_msg.linear.y = 0.0
        twist_msg.linear.z = 0.0
        twist_msg.angular.x = 0.1
        twist_msg.angular.y = 0.0
        twist_msg.angular.z = 0.0
        cmd_vel_pub.publish(twist_msg)

    def _send_twist_message(self, robot_id):
        self.get_logger().warn('Sending twist message!')
        cmd_vel_pub = self.create_publisher(Twist, f'/robot{robot_id}/cmd_vel', 10)
        twist_msg = Twist()
        twist_msg.linear.x = 0.1
        twist_msg.linear.y = 0.0
        twist_msg.linear.z = 0.0
        twist_msg.angular.x = 0.1
        twist_msg.angular.y = 0.0
        twist_msg.angular.z = 0.0
        cmd_vel_pub.publish(twist_msg)

    def _send_twist_message_1(self, robot_id):
        self.get_logger().warn('Sending twist message!')
        cmd_vel_pub = self.create_publisher(Twist, f'/robot{robot_id}/cmd_vel', 10)
        twist_msg = Twist()
        twist_msg.linear.x = 0.5
        twist_msg.linear.y = 0.1
        twist_msg.linear.z = 0.0
        twist_msg.angular.x = 0.1
        twist_msg.angular.y = 0.1
        twist_msg.angular.z = 0.0
        cmd_vel_pub.publish(twist_msg)

    def _get_twist_from_pose_pair(self, pose1: PoseStamped, pose2: PoseStamped):
        # Calculate a PID/twist message output from the pose inputs
        result_twist = Twist()
        return result_twist

    def _save_robot_initial_position(self, robot_id, pose_stamped: PoseStamped):
        initial_pose = Pose()
        initial_pose.position = pose_stamped.pose.position
        initial_pose.orientation = pose_stamped.pose.orientation
        ROBOT_CACHE[robot_id] = {"initial_pose": initial_pose}

    def _save_robot_current_position(self, robot_id, pose_stamped: PoseStamped):
        initial_pose = Pose()
        initial_pose.position = pose_stamped.pose.position
        initial_pose.orientation = pose_stamped.pose.orientation
        ROBOT_CACHE[robot_id] = initial_pose

    def _spawn_burger_bot_and_service(self, target_robot_id: int, initial_position: PoseStamped):
        robot_name = f'robot{target_robot_id}'
        x = initial_position.pose.position.x
        y = initial_position.pose.position.y
        z = initial_position.pose.position.z
        self.get_logger().info(f'Spawning robot with id {target_robot_id} at position {x}, {y}, {z}')
        test = subprocess.Popen(["ros2", "run", "crl_executer", "spawn_burger", robot_name, str(x), str(y), str(z)])
        robot_client = PathClient(robot_name)
        ROBOT_CACHE[target_robot_id]["client"] = robot_client

        self.get_logger().info(f'robot {target_robot_id} spawned successfully!')

    def _send_next_point_to_robot(self, target_robot_id: int, next_position: PoseStamped):
        robot_name = f'robot{target_robot_id}'
        x = next_position.pose.position.x
        y = next_position.pose.position.y
        z = next_position.pose.position.z
        self.get_logger().warn(f'Sending {robot_name} to position {x}, {y}, {z}')
        robot_client = ROBOT_CACHE[target_robot_id]["client"]
        robot_client.next_step(x, y, 0)
        robot_client.next_step(x, y, 0)  # solve the incapable of walking 180 deg from your position
        robot_client.next_step(x, y, 1)
        self.get_logger().info(f'Done current command')

    def _get_position_by_name(self, name):
        self.executer_tracker.get_pose(name)
        position = None
        while rclpy.ok():
            rclpy.spin_once(self.executer_tracker)
            if self.executer_tracker.future.done():
                response: GetEntityState.Response = self.executer_tracker.future.result()
                position = response.state.pose
                # x = response.state.pose.position.x
                # y = response.state.pose.position.y
                # _, _, yaw = euler_from_quaternion(response.state.pose.orientation)

                break

        return position

    def _construct_pose_stamped(self, position):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose = position
        return pose


def main(args=None):
    rclpy.init(args=args)
    multi_threaded_executer = MultiThreadedExecutor()
    node = Executer()
    multi_threaded_executer.add_node(node)
    try:
        node.get_logger().info('Starting Executer Node in multithreaded mode.\n')
        multi_threaded_executer.spin()
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt, shutting down.\n')
    # rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
