import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from goal_status_interface.msg import GoalStatus
from robot_status_interface.msg import RobotStatus
from robot_path_assignment_interface.msg import RobotPathAssignment

MAPF_PLAN_TOPIC = '/MAPF_PLAN'
ROBOT_STATUS_TOPIC = '/ROBOT_STATUS'
GOAL_STATUS_TOPIC = '/GOAL_STATUS'


class Executer(Node):
    def __init__(self):
        super().__init__('Executer')
        self.subscribe_to_mapf_plan_topic()
        self.expose_robot_status_topic()
        self.expose_goal_status_topic()

    def subscribe_to_mapf_plan_topic(self):
        self.plan_input_topic = self.create_subscription(RobotPathAssignment, MAPF_PLAN_TOPIC, self.send_plan_to_robot,
                                                         10)

    def expose_robot_status_topic(self):
        self.robot_status_topic = self.create_publisher(RobotStatus, ROBOT_STATUS_TOPIC, 10)

    def expose_goal_status_topic(self):
        self.goal_status_topic = self.create_publisher(GoalStatus, GOAL_STATUS_TOPIC, 10)


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

    def publish_robot_status(self):
        # TODO: depends on status from gazebo and optiTrack
        # This is just a guess at the format
        # msg = RobotStatus()
        # msg.robot_id = 5
        # msg.current_location.stamp.sec = 5
        # msg.current_location.stamp.nanosec = 5
        #
        # msg.current_location.position.x = 1
        # msg.current_location.position.y = 2
        # msg.current_location.position.z = 3
        #
        # msg.current_location.orientation.x = 1
        # msg.current_location.orientation.y = 2
        # msg.current_location.orientation.z = 3
        # msg.current_location.orientation.w = 4
        # self.robot_status_topic.publish(msg)
        pass

    def publish_goal_status(self):
        # TODO: depends on status from gazebo and optiTrack
        # This is just a guess at the format
        # msg = GoalStatus()
        # msg.goal_id = 5
        # msg.current_location.stamp.sec = 5
        # msg.current_location.stamp.nanosec = 5
        #
        # msg.current_location.position.x = 1
        # msg.current_location.position.y = 2
        # msg.current_location.position.z = 3
        #
        # msg.current_location.orientation.x = 1
        # msg.current_location.orientation.y = 2
        # msg.current_location.orientation.z = 3
        # msg.current_location.orientation.w = 4
        # self.goal_status_topic.publish(msg)
        pass

    def send_plan_to_robot(self, msg):
        # TODO: figure out how to correctly send plans to robots (NAV2/TWIST/something else?)
        target_robot_id = msg.target_robot_id
        task = msg.task
        if task == 'STOP':
            # Stop robot immediately
            pass
        elif task == 'START':
            # Tell robot to stop performing current tasks and begin a new path
            pass
        elif task == 'EXTEND':
            # Tell the robot to continue with these added assignments after it is done with current tasks
            pass
        # Find the correct robot and send him the task
        pass


def main(args=None):
    rclpy.init(args=args)
    node = Executer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
