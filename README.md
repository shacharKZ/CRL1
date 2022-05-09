# CRL1

If you want to make changes to the code, edit the python code as you usually would, then build using the command

```bash
colcon build --allow-overriding py_action_server test_action executer_interfaces
```

Remember that you ALWAYS need to source the workspace, you can do that from any terminal by changing your working directory to `crl_ws`/`CRL1` and running the command:
```bash
source ./install/setup.bash
```

In order to run the node manager after sourcing the workspace, use the command:

```bash
ros2 run py_action_server robot_manager_node [NUM_OF_ROBOTS]
```

In order to send a message to the node manager, use the command:

```bash
ros2 topic pub --once /robotManager executer_interfaces/PlanCommand "plan: 0:1,2,3;1:3,4,5"
```