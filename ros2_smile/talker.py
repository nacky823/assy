import rclpy
from  rclpy.node import Node
from std_msgs.msg import Int16

n = 0
pub =0

def main():
    global pub

    rclpy.init()
    node = Node("talker")
    pub = node.create_publisher(Int16, "/countup", 10)

    node.create_timer(0.5, cb)
    rclpy.spin(node)

def cb():
    global n
    msg = Int16()
    msg.data = n
    pub.publish(msg)
    n += 1

