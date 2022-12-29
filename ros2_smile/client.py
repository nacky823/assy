import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class Client():
    def __init__(self, nh):
        self.cli = nh.create_client(Spawn, "/times")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            print("waitting...")

    def request(self):
        req = Spawn.Request()
        req.name = "now"
        self.future = self.cli.call_async(req)

    def response(self, nh):
        while rclpy.ok():
            rclpy.spin_once(nh)
            if self.future.done():
                try:
                    self.res = self.future.result()
                except:
                    nh.get_logger().info("failed to response")
                else:
                    print(format(self.res.name))
                break

def main():
    rclpy.init()
    node = Node("client")
    client = Client(node)
    client.request()
    client.response(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

