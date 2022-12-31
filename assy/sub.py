import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("Count second : %d [s]" % msg.data)

rclpy.init()
node = Node("sub")
node.create_subscription(Int16, "/countsec", cb, 10)
rclpy.spin(node)
