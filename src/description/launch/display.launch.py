from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
import os
from ament_index_python.packages import get_package_share_path

def generate_launch_description():
    pkg_path = get_package_share_path('description')
    urdf_path = os.path.join(pkg_path, 'urdf', 'my_robot.urdf.xacro')
    rviz_config_path = os.path.join(pkg_path, 'rviz', 'urdf_config.rviz')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': Command(['xacro ', urdf_path])}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_path]
        ),
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{'use_sim_time': False}]
        ),
        # Launch the fake lidar Python script using ros2 run
        Node(
            package='description',
            executable='fake_lidar.py',
            output='screen'
        )
    ])
