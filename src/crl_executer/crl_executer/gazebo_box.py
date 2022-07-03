import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

'''
A launch file used to startup a Gazebo server and Gazebo client
The Server publishes a /get_entity_state service which allows for querying of robot and object positions in the gazebo scene
The Client starts up a Gazebo UI with the specified scene already loaded

This specific file loads the Turtlebot3 dqn_stage2 scene
'''
def generate_launch_description(map_name='turtlebot3_dqn_stage2.world'):
    # Sync robots and gazebo server time
    use_sim_time = LaunchConfiguration('use_sim_time', default='True')

    # Find Gazebo server directory
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    # chose the map to load (map_name)
    world = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'worlds',
        map_name
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )

    sim_time = ExecuteProcess(
        cmd=['ros2', 'param', 'set', '/gazebo', 'use_sim_time', use_sim_time],
        output='screen'
    )

    return LaunchDescription([gazebo, gzclient_cmd, sim_time])
