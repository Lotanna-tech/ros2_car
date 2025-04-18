# 🚗 ros2_car

A ROS 2 (Jazzy) simulation project featuring a mobile robot model with URDF/Xacro description, RViz visualization, and SLAM integration using a fake LIDAR node. Designed for running SLAM and navigation without needing Gazebo or real hardware.

## 💡 Description

`ros2_car` is a ROS 2 workspace package designed to simulate a car-like mobile robot using purely RViz and SLAM Toolbox, without the need for Gazebo. It includes:

- ✅ A custom URDF/Xacro robot model with joints and sensors
- ✅ Visualization in RViz2
- ✅ A fake LIDAR publisher (`/scan` topic) for simulating 2D laser scans
- ✅ Integration with `slam_toolbox` to enable SLAM with fake data
- ✅ Launch files for bringing up the robot, RViz, and SLAM toolbox together

## 📁 Structure

