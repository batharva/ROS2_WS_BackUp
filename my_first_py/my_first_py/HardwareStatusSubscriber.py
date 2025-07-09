#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus  
class HardwareStatusSubscriberNode(Node):
    def __init__(self):
        super().__init__('hardware_status_subscriber')
        self.subscription = self.create_subscription(
            HardwareStatus,
            'hardware_status',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: Temperature={msg.temperature}, Motors Ready={msg.are_motors_ready}, Debug Message="{msg.debug_message}"')
def main(args=None):
    rclpy.init(args=args)
    node = HardwareStatusSubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()