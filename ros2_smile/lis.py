import rclpy
from rclpy.node import Node
from smile_msgs.srv import Greet

def main():
    rclpy.init()
    node = Node("lis")
    client = node.create_client(Greet, "/greet")
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('waiting...')

    req = Greet.Request()
    req.name = "joker"
    furure = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failse call')
            else:
                node.get_logger().info("age: []".format(response.age))
                
            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

