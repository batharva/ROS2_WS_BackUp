#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedStateArray
from my_robot_interfaces.srv import SetLed

class BatteryClientNode(Node):
    def __init__(self):
        super().__init__('battery_client_node')
        self.battery_state_ ="full"
        self.last_time_battery_check_ = self.get_current_time_seconds()
        self.set_led_client_ = self.create_client(SetLed, 'set_led_state')
        self.battery_timer_ = self.create_timer(0.1, self.check_battery_status)
        self.get_logger().info("Battery Client Node has been started.")
    def get_current_time_seconds(self):
        seconds,nanoseconds= self.get_clock().now().seconds_nanoseconds()
        return seconds + nanoseconds / 1000000000.0
    def check_battery_status(self):
        time_now_ = self.get_current_time_seconds()
        if self.battery_state_== "full": 
            if time_now_ - self.last_time_battery_check_ > 4.0:
                self.battery_state_ = "empty"
                self.get_logger().info("Battery is empty! Charging...")
                self.call_set_led(2,1)
                self.last_time_battery_check_ = time_now_
        elif self.battery_state_ == "empty":
            if time_now_ - self.last_time_battery_check_ > 6.0:
                self.battery_state_ = "full"
                self.get_logger().info("Battery is full!")
                self.call_set_led(2,0)
                self.last_time_battery_check_ = time_now_

    def call_set_led(self, led_number,led_state):
        while not self.set_led_client_.wait_for_service(1.0):
            self.get_logger().info('Service not available, waiting again...')
        request = SetLed.Request()
        request.led_number = led_number
        request.led_state = led_state
        future = self.set_led_client_.call_async(request)
        future.add_done_callback(self.callback_call_set_led)
    def callback_call_set_led(self,future):
        response: SetLed.Response= future.result()
        if response.success:
            self.get_logger().info("Led Turn on")
        else:
            self.get_logger().error("Failed to turn on led")
def main(args=None):
    rclpy.init(args=args)
    node = BatteryClientNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()