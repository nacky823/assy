import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def main():
    rclpy.init()
    node = Node("lis")
    client = node.create_client(AddTwoInts, "/greet")
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('waiting...')

    req = AddTwoInts.Request()
    req.a = 3
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failse call')
            else:
                node.get_logger().info("addtest: {}".format(response.sum))
                
            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

