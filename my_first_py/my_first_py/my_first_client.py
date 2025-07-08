#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial

class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client_ = self.create_client(AddTwoInts,"add_two_ints")
    
    def call_add_two_ints(self, a,b):
        while not self.client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for AddTwoInts server.")
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = self.client_.call_async(request)
        future.add_done_callback(partial(self.callback_add_two_ints,request=request))
    
    def callback_add_two_ints (self,future,request):
        response = future.result()
        self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClientNode()
    node.call_add_two_ints(2,5)
    node.call_add_two_ints(1,4)
    node.call_add_two_ints(11,51)

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

# #!/usr/bin/env python3
# import rclpy
# from rclpy.node import Node
# from example_interfaces.srv import AddTwoInts

# def main(args=None):
#     rclpy.init(args=args)
#     node = Node("add_two_ints_client")
#     client = node.create_client(AddTwoInts,"add_two_ints")
#     while not client.wait_for_service(1.0):
#         node.get_logger().warn("Waiting for AddTwoInts Server.")
#     request = AddTwoInts.Request()
#     request.a = 1
#     request.b = 3

#     future = client.call_async(request)
#     rclpy.spin_until_future_complete(node, future)
#     response = future.result()
#     node.get_logger().info(f"{request.a} + {request.b} = {response.sum}")
#     rclpy.shutdown()

# if __name__ == "__main__":
#     main()
