#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedStateArray
from my_robot_interfaces.srv import SetLed

class LedPanelNode(Node):
    def __init__(self):
        super().__init__('led_panel_node')
        self.led_states_ = [0, 0, 0]  # Initialize LED states to off
        self.led_state_publisher = self.create_publisher(LedStateArray, 'led_states', 10)
        self.led_state_timer = self.create_timer(5.0, self.publish_led_states)
        self.set_led_service = self.create_service(SetLed, 'set_led_state', self.callback_set_led_state)
        self.get_logger().info('LED Panel Node has been started.')

    def publish_led_states(self):
        msg = LedStateArray()
        msg.led_states = self.led_states_
        self.led_state_publisher.publish(msg)

    def callback_set_led_state(self, request, response):
        led_number_ = request.led_number 
        led_state_ = request.led_state

        if led_number_ >= len(self.led_states_) or led_number_ < 0:
            response.success = False
            return response
        if led_state_ not in [0, 1]:
            response.success = False
            return response

        self.led_states_[led_number_] = led_state_
        response.success = True
        return response

def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()