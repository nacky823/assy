import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class Service():

    MAX_RES_CNT = 1

    def __init__(self, nh):
        srv = nh.create_service(Spawn, "/selection", self.cb)

    def cb(self, req, res):    
        if req.name == "The selection entered.":
            res.name = "connect"
        else:
            res.name = "Unable to meet request."

        return res

def main():
    rclpy.init()
    node = Node("selection")
    service = Service(node)
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

