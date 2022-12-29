import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class Service():
    def __init__(self, nh):
        self.srv = nh.create_service(Spawn, "/time_zone", self.cb)

    def cb(self, self.req, self.res):
        if self.req.name == "now":
            self.res.name = "夜"
        else:
            self.res.name = "nolibra"

        return self.res




def main():
    rclpy.init()
    node = Node("time_zone")
    service = Service(node)
    rclpy.spin(node)

if __name__ == "__main__":
    main()

