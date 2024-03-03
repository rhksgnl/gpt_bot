#include<iostream>
#include"interfaces/srv/gptsrv.hpp"
#include"rclcpp/rclcpp.hpp"
#include <memory>
#include <string>
#include <typeinfo>
#include "geometry_msgs/msg/twist.hpp"
#include "sensor_msgs/msg/joint_state.hpp"

using GptSrv = interfaces::srv::Gptsrv;
using Twist = geometry_msgs::msg::Twist;

class CentralNode : public rclcpp::Node
{
  private :
    rclcpp::Service<GptSrv> ::SharedPtr service_;
    std::string func_name_;
    std::string arguments_;

    void handle_service_request(const std::shared_ptr<GptSrv::Request> request,const std::shared_ptr<GptSrv::Response> response)
    {
      std::string func=request->a.c_str();
      devide_function(func);
      if(func_name_=="move"){
        move(std::stoi(arguments_));
      }
    }
    void joint_state_callback (int a , int b){

    }
  public :
    CentralNode() : Node("central_node"){
      service_ =this->create_service<GptSrv>("/gpt_service", std::bind(&CentralNode::handle_service_request, this, std::placeholders::_1, std::placeholders::_2));
    }
    void devide_function(std::string func){
      size_t pos = func.find('(');
      if (pos != std::string::npos) {
          func_name_ = func.substr(0, pos);
      } else {
          func_name_ = func;
      }

      if (pos != std::string::npos) {
          size_t end = func.find(')', pos);
          if (end != std::string::npos) {
              arguments_ = func.substr(pos + 1, end - pos - 1);
          }
      }
      std::cout << "function_name: " << func_name_ << std::endl;
      std::cout << "argumet: " << arguments_ << std::endl;
    }
    void move(int distance){
      auto twist_msg = std::make_shared<Twist>();
      twist_msg->linear.x = 1.0;


      }
};


int main (int argc,char **argv){
  rclcpp::init(argc, argv);
  auto node = std::make_shared<CentralNode>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
