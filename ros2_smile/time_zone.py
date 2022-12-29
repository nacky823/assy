import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn


class Service():
    def __init__(self, nh):
        self.srv = nh.create_service(Spawn, "/time_zone", self.cb)

    def cb(self, req, res):    
        if req.name == "now":
            res.name = "夜"
        else:
            res.name = "nolibra"
    
        return res




def main():
    rclpy.init()
    node = Node("time_zone")
    service = Service(node)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

