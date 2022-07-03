# CRL - Executer Component

This repository holds the code for the CRL Executer component.

In addition, this repository also holds the code for the varying ROS2 message interfaces used by the Executer.

This repository is also shipped with a mock_publisher package used to create mocked plans and send them to the executer for simulations.

## Requirements

In order to correctly run the code in this repository and use the Executer package the following need to be installed

- **Operating System:** Ubuntu 20.04 LTS
- **ROS:** ROS2, tested for Galactic and Foxy
- **Additional packages:** Gazebo, Turtlebot3, Turtlebot3 Simulations

ROS2 installation should be performed using packages as shown in the [ROS2 Tutorial](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html#ubuntu-debian)

Gazebo and Turtlebot3 installation should be performed as shown in the [Robotis Turtlebot3 PC Setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup) tutorial (be sure to switch to Foxy at the top of the page)

Turtlebot3 simulations should be installed as shown in the [Robotis Turtlebot3 Simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/) tutorial (be sure to switch to Foxy at the top of the page)

**Important!** - Always remember to source the ROS2 packages you are going to use and to export the correct shell variables, at the very minimum you need the following in your `.bashrc` file (assuming you cloned the Turtlebot3 Simulations repository to your users homedir `~/`):

```shell
source /opt/ros/<galactic/foxy>/setup.bash
source ~/turtlebot3_ws/install/setup.bash
export ROS_DOMAIN_ID=22
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/turtlebot3_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models
```

### Setting up the map files

In order for the executer to query the location of robots in the Gazebo scene, an update to the map files needs to be performed.

For every map file you want to use, add the following set of lines under the `<world name="default">` which is usually at the top of a gazebo `.world` file:

```xml
<plugin name="gazebo_ros_state" filename="libgazebo_ros_state.so">
  <ros>
    <namespace></namespace>
    <argument>model_states:=model_states_demo</argument>
    <argument>link_states:=link_states_demo</argument>
  </ros>

  <update_rate>1.0</update_rate>
</plugin>
```

For example, let's say we want to update the `empty_world.world` file that ships with Turtlebot3 Simulations, the file will be located under `<CLONE_DIR>/turtlebot3_ws/src/turtlebot3_simulations/turtlebot3_gazebo/worlds/empty_world.world` (where CLONE_DIR is where you cloned the [https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git](https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git) repository to).

The top part of the file will originally look like this:

```xml
<?xml version="1.0"?>
<sdf version="1.6">
  <world name="default">

    <include>
      <uri>model://ground_plane</uri>
    </include>

    <include>
      <uri>model://sun</uri>
    </include>

    <scene>
      <shadows>false</shadows>
    </scene>
...
```

After adding the plugin, the file will look like this:

```xml
<?xml version="1.0"?>
<sdf version="1.6">
  <world name="default">

    <plugin name="gazebo_ros_state" filename="libgazebo_ros_state.so">
      <ros>
        <namespace></namespace>
        <argument>model_states:=model_states_demo</argument>
        <argument>link_states:=link_states_demo</argument>
      </ros>

      <update_rate>1.0</update_rate>
    </plugin>

    <include>
      <uri>model://ground_plane</uri>
    </include>

    <include>
      <uri>model://sun</uri>
    </include>

    <scene>
      <shadows>false</shadows>
    </scene>
...
```

The plugin addition should be performed for every Gazebo scene you wish to use.

### Setting up the Executer

After installing ROS2 and the required packages clone this repo (we will refer to the clone directory as `crl_ws`), `cd` into the directory and run the build command:

```shell
colcon build
```

This command will build the ROS2 Interface messages, and crl_executer package and the mock_publisher package

## Running an Executer Simulation

Launching a simulation using the `crl_executer` and the `mock_publisher` includes 3 steps:

1. Startup the Gazebo scene (Gazebo Setup)
2. Startup the Executer (Executer Setup)
3. Startup the mock Publisher (Publisher Setup)

For example, if we want to run a simulation in the Gazebo empty world scene:

### Gazebo Setup

1. Open a terminal, `cd` to the `crl_ws` directory
2. source the packages by running the command `. install/setup.bash`
3. Startup Gazebo with the empty map using the command `ros2 launch ./src/crl_executer/crl_executer/gazebo.py`
   1. If instead you want to run the `world` scene, you would run `ros2 launch ./src/crl_executer/crl_executer/gazebo_world.py`
   2. And for every other scene you simply make a copy of one of the `gazebo_*.py` files and update the map path you want

You should see the Gazebo client starting up with the scene you chose

### Executer Setup

1. Open a terminal, `cd` to the `crl_ws` directory
2. source the packages by running the command `. install/setup.bash`
3. Startup the Executer using the command `ros2 run crl_executer executer`

You should see some initial logging messages sent from the Executer Node, also by running `ros2 topic list` you should see topics generated or subscribed to by the `executer`
   
### Publisher Setup

1. Open a terminal, `cd` to the `crl_ws` directory
2. source the packages by running the command `. install/setup.bash`
3. Startup the Publisher with a mocked plan using the command `ros2 run mock_publisher publisher --ros-args -p plan:="./plans_to_run/empty_demo.txt"`

You should see the formatted plan message generated by the Mock Publisher

At the end of the process you should see the Gazebo client showing the different agents as they are moving in the scene.

### Querying additional data

If you want to look at the contents of the `/robotStatus` topic:

1. Open a terminal, `cd` to the `crl_ws` directory
2. source the packages by running the command `. install/setup.bash`
3. Look at the message stream from the `/robotStatus` topic by running the command: `ros2 topic echo /robotStatus`

If you want to look at the contents of the `/goalStatus` topic:

1. Open a terminal, `cd` to the `crl_ws` directory
2. source the packages by running the command `. install/setup.bash`
3. Look at the message stream from the `/goalStatus` topic by running the command: `ros2 topic echo /goalStatus`

**Note:** The `/goalStatus` topic will only publish messages if the plan text file has goals in it, for an example file with goals speicifed, look at the [plan2.txt](./plans_to_run/plan2.txt) file under the `plans_to_run` directory

### Included Interfaces

The following interfaces are included in this repository:

- GoalStatus - used to report goals to the `/goalStatus` topic
- RobotStatus - used to report the status of each robot to the `/robotStatus` topic periodically
- RobotPathAssignment - used to specify a plan for a single robot
- RobotPathAssignmentPlan - a wrapper interface for an array of `RobotPathAssignment` messages
- Position - a service interface used by the Position service to report the position of a robot back to the `Executer` 