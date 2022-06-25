import rclpy
from rclpy.node import Node
from multi_burger_interfaces.srv import Position
from time import sleep


class PathClient(Node):
    def __init__(self, node_name: str) -> None:
        super().__init__(node_name)
        self.name = node_name
        self.client = self.create_client(Position, f'{self.name}_service')
        if not self.client.service_is_ready():
            self.client.wait_for_service()

        self.req = Position.Request()

    def next_step(self, x, y, act):
        self.req.x = float(x) / 2 + 0.25
        self.req.y = float(y) / 2 + 0.25
        self.req.action = act

        self.future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        if self.future.result() is not None:
            print('response: %r' % self.future.result())

        sleep(0.1)


def get_path(file, name):
    import yaml

    with open(file) as f:
        return yaml.safe_load(f)[name]


def main():
    import sys

    argv = sys.argv[1:]
    name = argv[0]
    path_file = argv[1]

    path = get_path(path_file, name)

    rclpy.init()

    bot1 = PathClient(name)
    for x, y, act in path:
        if act == 2:
            sleep(5)
        bot1.next_step(y, x, act)

    bot1.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

