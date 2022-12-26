import rclpy
from  rclpy.node import Node
from smile_msgs.msg import Smile

n = 0

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Smile, "/smile", 10)

node.create_timer(0.5, cb)
rclpy.spin(node)

def cb():
    global n
    msg = Smile()
    msg.name = "joker"
    msg.age = n
    pub.publish(msg)
    n += 1

