import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class SelectService():
    def __init__(self, nh):
        self.repeat = 1
        srv = nh.create_service(Spawn, "/select", self.cb)

    def cb(self, req, res):    
        if req.name == "p":
            self.sel = req.name
            res.name = "connect"
        elif req.name == "ending_password_hogehoge_soiya":
            self.repeat = 0
            res.name = "end"
        else:
            res.name = "Unable to meet request."

        return res

def main():
    rclpy.init()
    node = Node("order")
    service = SelectService(node)
    while service.repeat == 1:
        rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

