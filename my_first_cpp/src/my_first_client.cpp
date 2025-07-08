#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"
using namespace std::chrono_literals;
using namespace std::placeholders;
class AddTwoIntsClientNode : public rclcpp::Node 
{
public:
    AddTwoIntsClientNode() : Node("add_two_ints_client") {
        client_ = this->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");

    }
    void callAddTwoInts(int a, int b){
        while (!client_->wait_for_service(1s))
        {
            RCLCPP_WARN(this->get_logger(),"Waiting for the server to be up.");
        }
        auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
        request->a= a;
        request->b=b;
        client_->async_send_request(request,std::bind(&AddTwoIntsClientNode::callbackAddTwoInts,this,_1));
    }
private:
    void callbackAddTwoInts(rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedFuture future){
        auto response = future.get();
        RCLCPP_INFO(this->get_logger(),"Sum is %d",(int)response->sum);
    }
    rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedPtr client_;
};

int main(int argc, char **argv) {

    rclcpp::init(argc, argv);
    auto node = std::make_shared<AddTwoIntsClientNode>();
    node->callAddTwoInts(10,3);
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}


// #include "rclcpp/rclcpp.hpp"
// #include "example_interfaces/srv/add_two_ints.hpp"
// using namespace std::chrono_literals;
// int main(int argc, char **argv) {
//     rclcpp::init(argc, argv);
//     auto node = std::make_shared<rclcpp::Node>("add_two_ints_client");
//     auto client = node->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");
//     while (!client->wait_for_service(1s))
//     {
//         RCLCPP_WARN(node->get_logger(),"Wating for the server to be up.");
//     }
//     auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
//     request->a = 3;
//     request->b = 5;

//     auto future = client->async_send_request(request);
//     rclcpp::spin_until_future_complete(node,future);
//     auto response = future.get();
//     RCLCPP_INFO(node->get_logger(),"%d + %d = %d",(int)request->a,(int)request->b,(int)response->sum);

//     rclcpp::shutdown();
//     return 0;
// }
