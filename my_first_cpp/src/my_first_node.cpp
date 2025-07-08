#include "rclcpp/rclcpp.hpp"

class MyNode : public rclcpp::Node {
public:
    MyNode() : Node("cpp_test"),counter_(0) {
        timer_ = create_wall_timer(
            std::chrono::seconds(1),
            std::bind(&MyNode::timerCallback,this)
        );
    }

private:
    void timerCallback() {
        RCLCPP_INFO(get_logger(), "SNEHA %d",counter_);
        counter_++;
    }

    rclcpp::TimerBase::SharedPtr timer_;  
    int counter_;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MyNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}


// TEMPLATE
// #include "rclcpp/rclcpp.hpp"

// class MyCustomNode : public rclcpp::Node 
// {
// public:
//     MyCustomNode() : Node("node_name") {
//         RCLCPP_INFO(this->get_logger(), "MyCustomNode has been started");
//     }
// };

// int main(int argc, char **argv) {
//     rclcpp::init(argc, argv);
//     auto node = std::make_shared<MyCustomNode>();
//     rclcpp::spin(node);
//     rclcpp::shutdown();
//     return 0;
// }
