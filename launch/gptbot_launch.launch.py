import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (DeclareLaunchArgument, GroupAction,
                            IncludeLaunchDescription, SetEnvironmentVariable)
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.actions import PushROSNamespace
from launch_ros.descriptions import ParameterFile
from nav2_common.launch import RewrittenYaml, ReplaceString

def generate_launch_description():
  map_dir = LaunchConfiguration('$Home/map.yaml')
  launch_dir=os.path.join
    return LaunchDescription([
        Node(
            package='gptbot',
            namespace='gptbot',
            executable='goalpose',
            name='goal'
        ),
        
        Node(
            package='gptbot',
            namespace='gptbot',
            executable='initialpose',
            name='initial'
        ),
        IncludeLaunchDescription(
          PythonLaunchDescriptionSource(os.path.join(launch_dir,))
        )
    ])