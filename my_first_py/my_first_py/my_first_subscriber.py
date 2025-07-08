#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
class RobotNewsSubscriberNode(Node):
    def __init__(self):
        super().__init__("robot_news_subscriber")
        self.subscriber_= self.create_subscription(String,"robot_news_msg",self.callback_robot_news_msg,10)
        self.counter_=0
        self.get_logger().info("Robot Has Started Reciving Msg:")
    def callback_robot_news_msg(self,msg: String):
        self.get_logger().info(f"{self.counter_}"+"."+msg.data)
        self.counter_+=1
    
def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
    main()