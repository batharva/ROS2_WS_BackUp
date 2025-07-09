import rclpy
from rclpy.node import Node 
from my_robot_interfaces.srv import ComputeRectangleArea

class ComputeRectangleAreaServerNode(Node):
    def __init__(self):
        super().__init__('compute_rectangle_area_server')
        self.srv = self.create_service(ComputeRectangleArea, 'compute_rectangle_area', self.compute_area_callback)

    def compute_area_callback(self, request, response):
        response.area = request.length * request.width
        self.get_logger().info(f'Requested length: {request.length}, width: {request.width}, computed area: {response.area}')
        return response
def main(args=None):
    rclpy.init(args=args)
    node = ComputeRectangleAreaServerNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()