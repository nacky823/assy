import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import datetime

class Service():

    MAX_RES_CNT = 2
    DIFF_UTC = 9

    def __init__(self, nh):
        self.res_cnt = 0
        srv = nh.create_service(Spawn, "/times", self.cb)

    def cb(self, req, res):    
        if req.name == "now":
            res.name = self.times()
            self.res_cnt += 1
        else:
            res.name = "Unable to meet request."

        return res

    def times(self):
        time_diff = datetime.timedelta(hours=self.DIFF_UTC)
        time_zone = datetime.timezone(time_diff)
        now = datetime.datetime.now(time_zone)
        nowhm = now.strftime("%H:%M")
        send = str(nowhm) + "," + str(now.hour)

        return send

def main():
    rclpy.init()
    node = Node("times")
    service = Service(node)
    while not service.res_cnt == service.MAX_RES_CNT:
        rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

