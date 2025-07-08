#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class RobotNewsSubscriberNode : public rclcpp::Node 
{
public:
    RobotNewsSubscriberNode() : Node("robot_news_subscriber") {
        subscriber_ =  this->create_subscription<example_interfaces::msg::String>("robot_news_msg",10,
        std::bind(&RobotNewsSubscriberNode::callback_robot_news,this,std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(),"Robot News Station Is Listening:");
    }
private:
    void callback_robot_news(const example_interfaces::msg::String::SharedPtr msg){
        RCLCPP_INFO(this->get_logger(),"%s",msg->data.c_str());
    }
    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewsSubscriberNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}