#include "central_node.hpp"
#include <stdio.h>
#include <iostream>
    void CentralNode::handle_service_request(const std::shared_ptr<GptSrv::Request> request,const std::shared_ptr<GptSrv::Response> response)
    {
      std::string func=request->a.c_str();
      devide_function(func);
      if(func_name_=="move"){
        std::cout <<arguments_<<std::endl;
        move(std::stoi(arguments_));
        response->result = 1;
      }else{
        response->result=0;
      }
      RCLCPP_INFO(this->get_logger(),"서비스 콜백 종료");
    }
    void CentralNode::joint_state_callback (const sensor_msgs::msg::JointState::SharedPtr joint_state_msg){
      encoder_cnt=joint_state_msg->position[0];
      RCLCPP_INFO(this->get_logger,"아...")
    }

    CentralNode::CentralNode() : Node("central_node"){
      service_ =this->create_service<GptSrv>("/gpt_service", std::bind(&CentralNode::handle_service_request, this, std::placeholders::_1, std::placeholders::_2));
      twist_pub_ = this->create_publisher<geometry_msgs::msg::Twist>("/cmd_vel", 10);
      joint_st_sub_ = this->create_subscription<sensor_msgs::msg::JointState>("encoder_data", 10, std::bind(&CentralNode::joint_state_callback, this, std::placeholders::_1));
    }

    void CentralNode::devide_function(std::string func){
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
    }

    void CentralNode::move(int distance){
      auto twist_msg = std::make_shared<Twist>();
      float speed=0.0;
      while((encoder_cnt%10) < 4*distance){
            std::cout <<"와일문 탈출 못함"<<std::endl;
            std::cout<<encoder_cnt<<std::endl;
        twist_msg->linear.x = speed;
        twist_pub_->publish(*twist_msg);
        if(speed>1.0){speed=1.0;}
        else{speed+=0.00001;}
      }

      twist_msg->linear.x=0.0;
      twist_msg->linear.y=0.0;
      twist_msg->linear.z=0.0;
      twist_pub_->publish(*twist_msg);
      }


int main (int argc,char **argv){
  rclcpp::init(argc, argv);
  auto node = std::make_shared<CentralNode>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
