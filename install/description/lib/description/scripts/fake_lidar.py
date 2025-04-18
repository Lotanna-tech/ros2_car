
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math
import random

class FakeLidar(Node):
    def __init__(self):
        super().__init__('fake_lidar')
        self.publisher_ = self.create_publisher(LaserScan, 'scan', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        scan = LaserScan()
        scan.header.frame_id = 'lidar_link'
        scan.header.stamp = self.get_clock().now().to_msg()
        scan.angle_min = -math.pi / 2
        scan.angle_max = math.pi / 2
        scan.angle_increment = math.pi / 180
        scan.range_min = 0.2
        scan.range_max = 10.0
        scan.ranges = [random.uniform(1.0, 5.0) for _ in range(180)]
        self.publisher_.publish(scan)

def main(args=None):
    rclpy.init(args=args)
    node = FakeLidar()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
