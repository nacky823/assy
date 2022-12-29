import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn


def cb(req, res):
    if req.name == "now":
        res.name = "夜"
    else:
        res.name = "nolibra"

    return res




def main():
    rclpy.init()
    node = Node("time_zone")
    srv = node.create_service(Spawn, "/time_zone", cb)
    rclpy.spin(node)

if __name__ == "__main__":
    main()

