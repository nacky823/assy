import rclpy
from  rclpy.node import Node
from smile_msgs.srv import Greet

def cb(request, response):
    if request.name == "joker":
        response.age = 44
    else :
        response.age = 0

    return response

rclpy.init()
node = Node("tas")
srv = node.create_service(Greet, "greet", cb)
rclpy.spin(node)
