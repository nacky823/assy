import rclpy
from  rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self,nh):
        nh.create_timer(0.5, self.cb)
        self.pub = nh.create_publisher(Int16, "/countup", 10)
        self.n = 0

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        print(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
