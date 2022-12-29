import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import datetime

class Service():
    def __init__(self, nh):
        srv = nh.create_service(Spawn, "/now_time", self.cb)

    def cb(self, req, res):    
        if req.name == "now":
            res.name = "夜"
        else:
            res.name = "Unable to meet request."

        return res

    def nt(self):
        JST_MINUS_UTC = 9
        time_diff = datetime.timedelta(hours=JST_MINUS_UTC)
        time_zone = datetime.timezone(time_diff)
        now = datetime.datetime.now(time_zone)
        now_h_m = now.strftime("%H:%M")
        print(now_h_m)
        




def main():
    rclpy.init()
    node = Node("time_zone")
    service = Service(node)
    service.nt()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

