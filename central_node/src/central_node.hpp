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
using JointState=sensor_msgs::msg::JointState;
class CentralNode : public rclcpp::Node
{
  private :
    rclcpp::Service<GptSrv> ::SharedPtr service_;
    std::string func_name_;
    std::string arguments_;
    rclcpp::Publisher<Twist>::SharedPtr twist_pub_;
    rclcpp::Subscription<JointState>::SharedPtr joint_st_sub_;
    int encoder_cnt;
    void handle_service_request(const std::shared_ptr<GptSrv::Request> request,const std::shared_ptr<GptSrv::Response> response);
    void joint_state_callback (const sensor_msgs::msg::JointState::SharedPtr joint_state_msg);
  public :
    CentralNode();
    void devide_function(std::string func);
    void move(int distance);
};
