import rclpy
from  rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node = Node("talker")
pub = node.create_publisher(String, "/str/input", 10)

def cb():
    txt = input()
    msg = String()
    msg.data = txt
    pub.publish(msg)
    print(msg)

node.create_timer(0.5, cb)
rclpy.spin(node)
