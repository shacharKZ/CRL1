import os
import sys
import rclpy
from ament_index_python.packages import get_package_share_directory
from gazebo_msgs.srv import SpawnEntity
from rclpy.node import Node
# from position_service import PositionService
from crl_executer.position_service import PositionService


class SpawnBurger(Node):
    def __init__(self, node_name: str, x, y, z) -> None:
        super().__init__(node_name)

        self.client = self.create_client(SpawnEntity, "/spawn_entity")
        if not self.client.service_is_ready():
            self.client.wait_for_service()

        sdf_file_path = os.path.join(
            get_package_share_directory("turtlebot3_gazebo"), "models",
            "turtlebot3_burger", "model.sdf")

        self.request = SpawnEntity.Request()
        self.request.name = node_name
        self.request.xml = open(sdf_file_path, 'r').read()
        self.request.robot_namespace = node_name
        self.request.initial_pose.position.x = x
        self.request.initial_pose.position.y = y
        self.request.initial_pose.position.z = z

        self.future = self.client.call_async(self.request)


def main():
    argv = sys.argv[1:]
    print(argv)
    name = argv[0]
    x = float(argv[1])
    y = float(argv[2])
    z = float(argv[3])

    rclpy.init()

    bot = SpawnBurger(name, x, y, z)
    rclpy.spin_until_future_complete(bot, bot.future)
    if bot.future.result() is not None:
        print('response: %r' % bot.future.result())

    bot.get_logger().info("Done! Shutting down node.")
    bot.destroy_node()

    service = PositionService(name)
    rclpy.spin(service)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
