import rclpy
from  rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self,nh):
        self.pub = nh.create_publisher(Int16, "/countup", 10)
        nh.create_timer(0.5, cb)
        self.n = 0

def cb():
    msg = Int16()
    msg.data = talker.n
    talker.pub.publish(msg)
    print(msg)
    talker.n += 1

rclpy.init()
node = Node("talker")
talker = Talker(node)
rclpy.spin(node)
