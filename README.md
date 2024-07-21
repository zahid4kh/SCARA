# SCARA
Calculating Forward/Inverse Kinematics for 4-DOF Manipulators

## InvKinScara.py

Enter the desired values for:

	 px, py, pz - End-effector coordinates;
	 a1, a2 - Link lengths;
	 tool_angle - Angle of the tool (possibly gripper) with respect to base frame;
 	 tcp - Tool Center Point;
  
  and get two sets of possible joint variables.


## scarafk.py

Change the DH parameters according to your robot's configurations.

	a1 = 398.5    # height from frame 0 to frame 1
	a2 = 320.6    # distance from frame 0 to frame 1 in X0 direction ; also length of link 1
	a3 = 320.0    # distance from frame 1 to frame 2 in X1 direction ; also length of link 2
	a4 = 173.0    # height from frame 1 to frame 2
	a5 = 294.0    # height from frame 2 to frame 3

Enter the desired values for joint variables:
 
 	th1 = np.radians(0.0)
	th2 = np.radians(0.0)
	th4 = np.radians(0.0)
	stroke = 0.0

This will print the transformation matrix showing the projection of the end-effector frame to the base frame:

	print(np.round(H0_4, 3))
