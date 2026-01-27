import os

import launch
import launch_ros
import launch_ros.parameter_descriptions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    description_pkg = get_package_share_directory("inspire_hand_description")
    default_xacro_path = os.path.join(description_pkg, "RH56F1", "right", "urdf", "RH56F1_R.xacro")
    default_rviz_config_path = os.path.join(description_pkg, "RH56F1", "right", "rviz", "right.rviz")

    model_arg = launch.actions.DeclareLaunchArgument(
        name="model",
        default_value=str(default_xacro_path),
        description="xacro model file path",
    )

    robot_description_value = launch_ros.parameter_descriptions.ParameterValue(
        launch.substitutions.Command(["xacro", launch.substitutions.LaunchConfiguration("model")]),
        value_type=str,
    )

    robot_state_publisher = launch_ros.actions.Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description_value}],
    )

    joint_state_publisher = launch_ros.actions.Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )

    rviz_node = launch_ros.actions.Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", default_rviz_config_path],
    )

    return launch.LaunchDescription(
        [model_arg, robot_state_publisher, joint_state_publisher, rviz_node]
    )
