from morse.builder import *

# pr2 robot with laser (scan) and odometry (odom) sensors, and actuators
#  for armature (joint_trajectory_contorller) asnd wheels (cmd_vel) to the scene
pr2 = NavPR2()
pr2.add_interface("ros")

# teleport actuator for the pr2
teleport_pr2 = Teleport()
pr2.append(teleport_pr2)
teleport_pr2.add_interface("ros", topic="pr2_teleport_pose")

# adding human model
human = Human()
human.properties(WorldCamera = True)

# pose sensor for the human
pose = Pose()
human.append(pose)
pose.add_interface("ros", topic="human_pose")

# teleport actuator for the human
teleport_human = Teleport()
human.append(teleport_human)
teleport_human.add_interface("ros", topic="human_teleport_pose")

# set the environment to laas_adream
env = Environment("laas_adream.blend", fastmode=True)
env.set_camera_location([18.0, 4.0, 10.0])
env.set_camera_rotation([1.0, 0.0 , 1.57])

# put the robot and human in some good places
pr2.translate(2.0, 2.0, 0.0)
human.translate(3.0, 3.0, 0.0)

# add clock
clock = Clock()
clock.add_interface("ros", topic="clock")
pr2.append(clock)
human.append(clock)

env.use_relative_time(True)
env.create()
