'''
Class for managing the state of the VIO systems.
'''
import pandas as pd

class VIOManager():

	def __init__(self):
		pass

	def get_state(self):
		pass

'''
A VIO manager that always return the ground-truth as the IMU state
'''
class GTVIOManager(VIOManager):

	def __init__(self, file_path):
		VIOManager.__init__(self)
		# read header first because we want to ignore the # character.
		headers = pd.read_csv(file_path, delim_whitespace=True, nrows=0).columns[1:]
		self.states = pd.read_csv(file_path, delim_whitespace=True, header=None, skiprows=1, names=headers)
		self.index = 0

	def get_state(self):
		# TODO: use a file reader for accessing these states, as currently
		pos = self.states.loc[self.index, ['tx', 'ty', 'tz']]
		quat = self.states.loc[self.index, ['qx', 'qy', 'qz', 'qw']]
		timestamp = self.states.loc[self.index, ['timestamp(s)']][0]
		imu_state = {'position': pos, 'quaternion': quat}
		state = {'imu': imu_state, 'timestamp': timestamp}
		self.index += 1
		return state

def test_GTVIOManager():
	print("Testing get state from ground truth trajectory.")
	path = "/home/jamesdi1993/workspace/catkin_ws_ov/src/open_vins/ov_data/uzh_fpv/indoor_forward_9_snapdragon_with_gt.txt"
	viomanager = GTVIOManager(path)
	state = viomanager.get_state()
	print("The state is: %s" % state)

if __name__=="__main__":
	test_GTVIOManager()