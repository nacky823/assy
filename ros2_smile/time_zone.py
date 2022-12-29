import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import datetime

class Service():
    def __init__(self, nh):
        srv = nh.create_service(Spawn, "/time_zone", self.cb)

    def cb(self, req, res):    
        if req.name == "now":
            res.name = "夜"
        else:
            res.name = "Unable to meet request."

        return res

    def tz(self):
        JST_MINUS_UTC = 9
        now = datetime.timedelta(hours=9)
        print(now)



def main():
    rclpy.init()
    node = Node("time_zone")
    service = Service(node)
    service.tz()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

