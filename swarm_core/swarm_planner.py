#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
import numpy as np

class SwarmPlanner(Node):
    def __init__(self):
        super().__init__('swarm_planner')
        self.publisher_target = self.create_publisher(PoseStamped, '/uav/target_waypoint', 10)
        self.subscription_consensus = self.create_subscription(String, '/mesh/consensus_state', self.consensus_callback, 10)
        self.timer = self.create_timer(0.1, self.cbba_allocation_loop)
        self.current_state = np.zeros(3)

    def consensus_callback(self, msg):
        data = msg.data.split(',')
        if len(data) >= 3:
            self.current_state = np.array([float(data[0]), float(data[1]), float(data[2])])

    def cbba_allocation_loop(self):
        target_msg = PoseStamped()
        target_msg.header.stamp = self.get_clock().now().to_msg()
        target_msg.header.frame_id = 'map'
        target_msg.pose.position.x = self.current_state[0] + 15.0
        target_msg.pose.position.y = self.current_state[1] + 15.0
        target_msg.pose.position.z = 10.0
        self.publisher_target.publish(target_msg)

def main(args=None):
    rclpy.init(args=args)
    node = SwarmPlanner()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
