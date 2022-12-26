import rclpy
from rclpy.node import Node
from smile_msgs.msg import Smile

def cb(msg):
    global node
    node.get_logger().info("Listen: %s" % msg)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Smile, "/smile", cb, 10)
rclpy.spin(node)
