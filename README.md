# ROS2 Serial - Blinking LED
This is a fork of the original code from <ins>docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html</ins>, with some changes.<br />
An Arduino MEGA board is used as the hardware where the blinking LED is actually happening.<br /><br />
ROS2 Humble - Arduino MEGA 2560<br />
## Essential Commands<br />
### Project
- `colcon build --symlink-install`<br />
- `cd <your_workspace>/src`<br />
- `ros2 pkg create --build-type ament_python --license Apache-2.0 <your_package>`<br />
### Arduino<br /> 
- `sudo chmod a+rw /dev/ttyACM0`<br />
### Operating<br /> 
- `source install/setup.bash`<br />
- `ros2 run <your_package> befehl`<br />
## Notes from the Tutorial<br /> 
### package.xml
After the lines above, add the following dependencies corresponding to your node’s import statements:<br />
- `<exec_depend>rclpy</exec_depend>`<br />
- `<exec_depend>std_msgs</exec_depend>`<br />
### setup.cfg
The contents of the setup.cfg file should be correctly populated automatically, like so:<br />
- `[develop]`<br />
- `script_dir=$base/lib/py_pubsub`<br />
- `[install]`<br />
- `install_scripts=$base/lib/py_pubsub`<br />
