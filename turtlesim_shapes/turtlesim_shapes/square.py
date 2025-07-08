# not working comeback again

# #!/usr/bin/env python3

# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# import math

# class TurtleSquareNode(Node):
#     def __init__(self):
#         super().__init__("turtle_square")
#         self.publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
#         self.timer_ = self.create_timer(0.1, self.move_square)  # 10 Hz

#         # State variables
#         self.state = "MOVE_FORWARD"
#         self.start_time = self.get_clock().now()
#         self.edge_count = 0

#     def move_square(self):
#         msg = Twist()
#         current_time = self.get_clock().now()
#         elapsed_time = (current_time - self.start_time).nanoseconds / 1e9  # seconds

#         if self.edge_count >= 4:
#             # Stop the turtle after drawing the square
#             msg.linear.x = 0.0
#             msg.angular.z = 0.0
#             self.publisher_.publish(msg)
#             self.get_logger().info("Finished drawing square.")
#             self.timer_.cancel()  # Stop the timer
#             return

#         if self.state == "MOVE_FORWARD":
#             msg.linear.x = 1.0  # Move forward
#             if elapsed_time >= 2.0:  # Move forward for 2 seconds
#                 self.state = "TURN"
#                 self.start_time = current_time
#         elif self.state == "TURN":
#             msg.angular.z = math.pi / 4  # 45 deg/sec → 90° in 2 sec
#             if elapsed_time >= 2.0:
#                 self.state = "MOVE_FORWARD"
#                 self.start_time = current_time
#                 self.edge_count += 1

#         self.publisher_.publish(msg)

# def main(args=None):
#     rclpy.init(args=args)
#     node = TurtleSquareNode()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == "__main__":
#     main()
