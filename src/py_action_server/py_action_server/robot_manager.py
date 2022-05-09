import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from executer_interfaces.msg import PlanCommand


class ExecuterPlanListener(Node):
    def __init__(self):
        super().__init__('ExecuterPlanListener')
        self.declare_parameter('number_of_robots', '0')
        self.number_of_robots = int(self.get_parameter('number_of_robots').value)
        self.publisher_dict = {}
        self.init_robot_publishers()
        self.subscriber_ = self.create_subscription(PlanCommand, '/robotManager', self.listener_callback, 10)

    def init_robot_publishers(self):
        for i in range(self.number_of_robots):
            self.get_logger().info(f'Creating publisher for robot robot{i}')
            self.publisher_dict[i] = self.create_publisher(Twist, f'/robot{i}/cmd_vel', 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'I received message: {msg}')
        self.parse_plan_message(msg)
        message = Twist()
        message.linear.x = 5.0
        message.linear.y = 0.0
        # assume we gave parameters to all of twist (linear+angular)
        # This command should work: if not, refer back to the publisher/subscriber example in ROS2 website
        self.publisher_dict[0].publish(message)
        # robot_id = msg.robotid0
        # x = msg.robot0x
        # y = msg.robot0y
        # self.get_logger().info(f'I\'m sending the message to the cmd_vel')
        # self.get_logger().info(f'Received: {robot_id}->[{x},{y}]')

    def parse_plan_message(self, msg):
        robot_plans = msg.plan.split(';')
        for plan in robot_plans:
            robot_id = plan.split(':')[0]
            x, y, z = (plan.split(':')[1]).split(',')
            self.get_logger().info(f'Received coords for robot {robot_id}: [{x},{y},{z}]')


# class ManagerNode(Node):
#     server_list = []
#     robot_coords_list = []
#
#     def __init__(self):
#         super().__init__('RobotManagerNode')
#
#         # semicolon(;) separates robots, colon(:) separates positions in a specific robot position list, comman(,) separates the X,Y of a specific postion
#         self.declare_parameter('robot_positions_list', "1,2;3,4")
#
#         param_test = self.get_parameter('robot_positions_list')
#         self.robot_coords_list = self.parse_coords_list(param_test.value)
#         print('result:')
#         print(self.parse_coords_list(param_test.value))
#
#         self.setup_servers()
#         # self.get_logger().info(f'Received param: {param_test.value}')
#
#     def setup_servers(self):
#         i = 0
#         for robot in self.robot_coords_list:
#             server = TestActionServer(robot[0], i)
#             self.get_logger().info(f'Spinning up server: {i}')
#             rclpy.spin(server)
#             self.get_logger().info(f'Finished spinning up server: {i}')
#             self.server_list.append(server)
#             i += 1
#
#     @staticmethod
#     def parse_coords_list(coords: str):
#         individual_robot_lists = coords.split(';')
#         robot_coords_list = []
#         for r_list in individual_robot_lists:
#             current_fixed_robot_coords = []
#             coord_pairs = r_list.split(':')
#             for coord_pair in coord_pairs:
#                 coord = coord_pair.split(',')
#                 current_fixed_robot_coords.append((float(coord[0]), float(coord[1]), 1.0, 0.0))
#             robot_coords_list.append(current_fixed_robot_coords)
#         return robot_coords_list
#
#
# class TestActionServer(Node):
#     navigator: BasicNavigator = None
#
#     def __init__(self, initial_pos, robot_id=0):
#         super().__init__('test_action_server')
#         self._action_server = ActionServer(
#             self,
#             Test,
#             f'my_action{robot_id}',
#             self.execute_callback)
#         self.publisher_ = self.create_publisher(PoseStamped, f'/robot{robot_id}/cmd_vel', 10)
#         self.navigator = BasicNavigator()
#
#         amcl_pose_qos = QoSProfile(
#           durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
#           reliability=QoSReliabilityPolicy.RELIABLE,
#           history=QoSHistoryPolicy.KEEP_LAST,
#           depth=1)
#
#         self.navigator.localization_pose_sub = self.navigator.create_subscription(PoseWithCovarianceStamped,
#                                                               f'/robot{robot_id}/amcl_pose',
#                                                               self.navigator._amclPoseCallback,
#                                                               amcl_pose_qos)
#         x, y, z, w = initial_pos
#         initial_pose = PoseStamped()
#         initial_pose.header.frame_id = 'map'
#         initial_pose.header.stamp = self.navigator.get_clock().now().to_msg()
#         initial_pose.pose.position.x = x
#         initial_pose.pose.position.y = y
#         initial_pose.pose.position.z = 0.1
#         initial_pose.pose.orientation.x = 0.0
#         initial_pose.pose.orientation.y = 0.0
#         initial_pose.pose.orientation.z = z
#         initial_pose.pose.orientation.w = w
#         self.navigator.setInitialPose(initial_pose)
#
#         # Wait for navigation to fully activate, since autostarting nav2
#         self.navigator.waitUntilNav2Active()
#
#     def execute_callback(self, goal_handle):
#         self.get_logger().info('Executing goal...')
#
#         ix, iy, iz, iw = self.get_coords_from_pos(self.navigator.initial_pose)
#         # Current action has list: [x,y,z,w]
#         x, y, z, w = goal_handle.request.pose
#         msg = PoseStamped()
#         msg.header.frame_id = 'map'
#         msg.header.stamp = self.navigator.get_clock().now().to_msg()
#         msg.pose.position.x = x
#         msg.pose.position.y = y
#         msg.pose.orientation.z = z
#         msg.pose.orientation.w = w
#
#         feedback_msg = Test.Feedback()
#         feedback_msg.feedback = "Robot moving to new location..."
#
#         self.navigator.goToPose(msg)
#
#         i = 0
#         while not self.navigator.isNavComplete():
#             i += 1
#             feedback = self.navigator.getFeedback()
#             if feedback and i % 5 == 0:
#                 feedback_string = f'timestep: {i % 5} - Estimated time of arrival from [{ix},{iy},{iz},{iw}] at [{x},{y},{z},{w}]' + ' for worker: ' + '{0:.0f}'.format(
#                     Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9) + ' seconds.'
#                 print(feedback_string)
#
#                 feedback_msg.feedback = feedback_string
#                 goal_handle.publish_feedback(feedback_msg)
#
#         goal_handle.succeed()
#
#         print('I am done')
#         # msg.linear.x = 0.0
#         # self.publisher_.publish(msg)
#
#         result = Test.Result()
#         result.status = f"Finished action server. Moved to position [{x},{y},{z},{w}]"
#         return result
#
#     @staticmethod
#     def get_coords_from_pos(pos: PoseStamped):
#         return pos.pose.position.x, pos.pose.position.y, pos.pose.orientation.z, pos.pose.orientation.w


def main(args=None):
    rclpy.init(args=args)
    node = ExecuterPlanListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
