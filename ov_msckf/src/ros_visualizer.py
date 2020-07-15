#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from nav_msgs.msg import Path
import numpy as np

class ROSVisualizer():

	def __init__(self, vio_manager):
		rospy.init_node('ROS_Visualizer')

		self.imu_publisher = rospy.Publisher('/ov_msckf/poseimu', PoseWithCovarianceStamped, queue_size=2)
		self.path_publisher = rospy.Publisher('/ov_msckf/pathimu', Path, queue_size=2)
		self.vio_manager = vio_manager
		self.poses_seq_imu = 0; # starting from 0
		self.poses_imu = []

	def publish_state(self):
		state = self.vio_manager.get_state();
		print("The state is: %s" % state)
		pose_msg = PoseWithCovarianceStamped();
		timestamp = state['timestamp']
		imu_state = state['imu']
		pose_msg.header.stamp = rospy.Time(timestamp);
		pose_msg.header.seq = self.poses_seq_imu;
		pose_msg.header.frame_id = "global";

		quat = imu_state['quaternion'];
		pos = imu_state['position'];
		pose_msg.pose.pose.orientation.x = quat[0];
		pose_msg.pose.pose.orientation.y = quat[1];
		pose_msg.pose.pose.orientation.z = quat[2];
		pose_msg.pose.pose.orientation.w = quat[3];
		pose_msg.pose.pose.position.x = pos[0];
		pose_msg.pose.pose.position.y = pos[1];
		pose_msg.pose.pose.position.z = pos[2];

		'''
		for r in range(0, 6):
			for c in range(0, 6):
				pose_msg.pose.covariance[6 * r+c] = 0;
		'''

		posetemp = PoseStamped();
		posetemp.header = pose_msg.header
		posetemp.pose = pose_msg.pose.pose
		self.poses_imu.append(posetemp)

		arrIMU = Path()
		arrIMU.header.stamp = rospy.Time.now()
		arrIMU.header.seq = self.poses_seq_imu
		arrIMU.header.frame_id = "global";
		arrIMU.poses = self.poses_imu
		self.path_publisher.publish(arrIMU);
		self.poses_seq_imu+= 1;

if __name__=='__main__':
	visualizer = ROSVisualizer(None)