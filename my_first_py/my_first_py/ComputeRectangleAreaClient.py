#!/usr/bin/env python3
# filepath: /home/atharva/ros2_ws/src/my_first_py/my_first_py/ComputeRectangleAreaClient.py
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import ComputeRectangleArea
from functools import partial

class ComputeRectangleAreaClientNode(Node):
    def __init__(self):
        super().__init__("compute_rectangle_area_client")
        self.client_ = self.create_client(ComputeRectangleArea, "compute_rectangle_area")

    def call_compute_rectangle_area(self, length, width):
        while not self.client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for ComputeRectangleArea server.")
        request = ComputeRectangleArea.Request()
        request.length = length
        request.width = width

        future = self.client_.call_async(request)
        future.add_done_callback(partial(self.callback_compute_rectangle_area, request=request))

    def callback_compute_rectangle_area(self, future, request):
        response = future.result()
        if response is not None:
            self.get_logger().info(
                f"Requested length: {request.length}, width: {request.width}, computed area: {response.area}"
            )
        else:
            self.get_logger().error("Service call failed")

def main(args=None):
    rclpy.init(args=args)
    node = ComputeRectangleAreaClientNode()
    node.call_compute_rectangle_area(5.0, 3.0)
    node.call_compute_rectangle_area(2.5, 4.5)
    node.call_compute_rectangle_area(10.0, 7.0)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()