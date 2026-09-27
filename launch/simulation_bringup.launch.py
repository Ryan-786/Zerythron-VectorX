import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    world_arg = DeclareLaunchArgument(
        'world',
        default_value='urban_disaster',
        description='Simulation world name'
    )
    
    swarm_planner_node = Node(
        package='zerythron_vector_x',
        executable='swarm_planner',
        name='swarm_planner_node',
        output='screen'
    )

    comms_manager_node = Node(
        package='zerythron_vector_x',
        executable='comms_manager',
        name='comms_manager_node',
        output='screen'
    )

    return LaunchDescription([
        world_arg,
        swarm_planner_node,
        comms_manager_node
    ])
