import rclpy
from  rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def cb(request, response):
    if request.a == 3:
        response.sum = 56
    else :
        response.sum = 22

    return response

rclpy.init()
node = Node("tas")
srv = node.create_service(AddTwoInts, "/greet", cb)
rclpy.spin(node)
