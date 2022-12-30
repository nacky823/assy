import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class Service():
    def __init__(self, nh):
        self.end_srv = 0
        self.select = "init"
        srv = nh.create_service(Spawn, "/selection", self.cb)

    def cb(self, req, res):    
        if req.name == "p":
            self.select = req.name
            res.name = "connect"
        elif req.name == "ending_password_hogehoge_soiya":
            self.end_srv = 1
            res.name = "end"
        else:
            res.name = "Unable to meet request."

        return res

def main():
    rclpy.init()
    node = Node("selection")
    service = Service(node)

    while service.end_srv == 0:
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

