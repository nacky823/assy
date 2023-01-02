#!/usr/bin/python3
# SPDX-FileCopyrightText: 2022 NAGAKI Yuki
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Second():
    def __init__(self, nh):
        self.pub = nh.create_publisher(Int16, "/countsec", 10)
        self.n = 0
        nh.create_timer(1.0, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Node("pub")
    second = Second(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
