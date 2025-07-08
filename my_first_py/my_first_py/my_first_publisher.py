#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode(Node):
    def __init__(self,sister_name):
        super().__init__("robot_news_station")
        self.publisher_ = self.create_publisher(String,"robot_news_msg",10)
        self.timer_ = self.create_timer(0.5,self.publisher_news)
        self.sister_name = sister_name
        self.get_logger().info("Robot News Station Is Publishing:")

    def publisher_news(self):
        msg= String()
        msg.data = f"{self.sister_name} Is My Sis."
        self.publisher_.publish(msg)

def main(args=None):
    sister_name = input("Entre Your Sister's Name:")
    rclpy.init(args=args)
    node = RobotNewsStationNode(sister_name)
    rclpy.spin(node)
    rclpy.shutdown(node)

if __name__== "__main__":
    main()

