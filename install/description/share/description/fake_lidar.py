#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math
import time

class FakeLidar(Node):
    def __init__(self):
        super().__init__('fake_lidar')
        self.publisher = self.create_publisher(LaserScan, '/scan', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.publish_scan)

    def publish_scan(self):
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'lidar_link'
        msg.angle_min = -math.pi
        msg.angle_max = math.pi
        msg.angle_increment = math.pi / 180
        msg.time_increment = 0.0
        msg.scan_time = 0.1
        msg.range_min = 0.1
        msg.range_max = 5.0
        msg.ranges = [2.0 + 0.1 * math.sin(i / 10.0) for i in range(360)]

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = FakeLidar()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
