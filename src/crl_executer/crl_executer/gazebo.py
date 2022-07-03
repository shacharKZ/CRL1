import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

'''
run this file with "ros2 launch ./src/crl_executer/crl_executer/gazebo.py"
in theory, you can run any gazebo map (world). just change the name of the 
default map_name arg.
note to added the following block of code in the map ".world" 
file (like "/opt/ros/galactic/share/turtlebot3_gazebo/world/empty_world.world"):

<plugin name="gazebo_ros_state" filename="libgazebo_ros_state.so">
      <ros>
        <namespace></namespace>
        <argument>model_states:=model_states_demo</argument>
        <argument>link_states:=link_states_demo</argument>
      </ros>

      <update_rate>1.0</update_rate>
</plugin>
    
'''
def generate_launch_description(map_name='empty_world.world'):
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
