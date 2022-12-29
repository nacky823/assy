import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class Client():
    def __init__(self, nh):
        self.client = nh.create_client(Spawn, "now_time")
        while not self.client.wait_for_service(timeout_sec=1.0):
            nh.get_logger().info("waitting...")

    def request(self):
        self.req = Spawn.Request()
        self.req.name = "now_time"
        self.future = self.client.call_async(self.req)
        
    def response(self, nh)
        while rclpy.ok():
            rclpy.spin_once(nh)
            if self.future.done():
                try:
                    self.res = self.future()
                except:
                    nh.get_logger().info("failed to response")
                else:
                    nh.get_logger().info("{}".format(self.res.name))
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

