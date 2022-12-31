import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

def main():
    rclpy.init()
    node = Node("sub")
    pub = node.create_subscription(Int16, "/countsec", cb, 10)
    rclpy.spin(node)

if __name__ = "__main__":
    main()
