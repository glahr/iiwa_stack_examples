# iiwa_stack_examples
Sample packages on how to extend [**iiwa_stack**](https://github.com/SalvoVirga/iiwa_stack).

This packages are used within the [**wiki of iiwa_stack**](https://github.com/SalvoVirga/iiwa_stack/wiki) to explain some concepts of its usage.     
[**iiwa_stack**](https://github.com/SalvoVirga/iiwa_stack) needs to be present on the system to make these packages work.

In brief, here is contained :
- **iiwa_tool**: packages that show an example of how to add a tool to the KUKA LBR IIWA description.
- **two_iiwa** : packages that show an example of how to work with two iiwas (in Gazebo).

## Python example

### Joint control

Run in first terminal:
```
roslaunch iiwa_gazebo iiwa_gazebo_with_sunrise.launch
```

Wait for the model to load, then, into another terminal:
```
rosrun iiwa_tool_examples joint_pos_ctrl_test.py
```
### Cartesian control
First terminal:
```
roslaunch iiwa_gazebo iiwa_gazebo_with_sunrise.launch
rosrun iiwa_tool_examples cartesian_pos_ctrl_test.py
```

### Moveit
```
roslaunch iiwa_gazebo iiwa_gazebo_with_sunrise.launch
roslaunch iiwa_tool_examples iiwa_tool_command_moveit.launch
```

### Actionlib

#### Joint control
```
roslaunch iiwa_sim iiwa_sim_roscontrol.launch
roslaunch iiwa_gazebo iiwa_gazebo.launch
rosrun iiwa_tool_examples joint_pos_ctrl_test_action.py
```

#### Cartesian control
```
roslaunch iiwa_sim iiwa_sim_roscontrol.launch
roslaunch iiwa_gazebo iiwa_gazebo.launch
rosrun iiwa_tool_examples cartesian_pos_ctrl_test_action.py
```
