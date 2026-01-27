# Inspire Hand Description

ROS 2 description package for Inspire Hand models. RH56F1 left/right assets live under `RH56F1/left` and `RH56F1/right` (URDF/XACRO, meshes, configs, RViz, legacy launch).

## Layout
- `RH56F1/left|right/urdf`: `*.xacro` and generated `*.urdf`/`*.csv`
- `RH56F1/left|right/meshes`: STL meshes referenced by the URDF
- `RH56F1/left|right/config`: joint name lists and related config
- `RH56F1/left|right/launch`: `display.launch.py` (ROS 2), `gazebo.launch` (ROS 1 legacy)
- `RH56F1/left|right/rviz`: saved RViz configs

## Quick use (ROS 2)
```
ros2 launch inspire_hand_description RH56F1/left/launch/display.launch.py
ros2 launch inspire_hand_description RH56F1/right/launch/display.launch.py
```
`display.launch.py` defaults to the packaged XACRO; override with `model:=/path/to/custom.xacro` if needed.

## Notes
- Paths inside URDF/XACRO were rewritten to `package://inspire_hand_description/RH56F1/{left|right}/...` so they remain valid after install.
- `gazebo.launch` files are ROS 1 style and kept only for reference. Use the ROS 2 display launchers above for visualization.
