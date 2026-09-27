#!/usr/init/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class CommsManager(Node):
    def __init__(self):
        super().__init__('comms_manager')
        self.publisher_status = self.create_publisher(String, '/mesh/network_status', 10)
        self.timer = self.create_timer(1.0, self.evaluate_link_quality)

    def evaluate_link_quality(self):
        pdr = round(random.uniform(92.0, 99.8), 2)
        latency = round(random.uniform(45.0, 120.0), 2)
        status_msg = String()
        status_msg.data = f"PDR:{pdr},LATENCY:{latency},HOPS:2,STATUS:OPTIMAL"
        self.publisher_status.publish(status_msg)

def main(args=None):
    rclpy.init(args=args)
    node = CommsManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
