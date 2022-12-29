import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import datetime

class Service():
    def __init__(self, nh):
        srv = nh.create_service(Spawn, "/time", self.cb)

    def cb(self, req, res):    
        if req.name == "now":
            res.name = self.times()
        else:
            res.name = "Unable to meet request."

        return res

    def times(self):
        JST_MINUS_UTC = 9
        time_diff = datetime.timedelta(hours=JST_MINUS_UTC)
        time_zone = datetime.timezone(time_diff)
        now = datetime.datetime.now(time_zone)
        nowhm = now.strftime("%H:%M")
        send = str(nowhm) + "," + str(now.hour)

        return send

def main():
    rclpy.init()
    node = Node("time_zone")
    service = Service(node)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

