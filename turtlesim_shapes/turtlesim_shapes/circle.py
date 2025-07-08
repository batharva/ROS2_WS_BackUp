#!/usr/bin.env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleCircleNode(Node):
    def __init__(self):
        super().__init__("turtle_circle")
        self.publisher_ = self.create_publisher(Twist,"turtle1/cmd_vel",10)
        self.timer_ = self.create_timer(0.1,self.move_circle)
    def move_circle(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 1.0
        self.publisher_.publish(msg)

    
def main(args=None):
    rclpy.init(args=args)
    node = TurtleCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()