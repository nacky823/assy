import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def cb(msg):
    global node
    node.get_logger().info("Listen: %s" % msg.data)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(String, "/str/input", cb, 10)
rclpy.spin(node)
