# coding:utf-8
# create by liuzhenbo 2020/8/16 in nwpu

import numpy as np

class Mappoint:
    def __init__(self):
        self._descriptor = 0
        self._pose = np.array([[0], [0]])
        self._seeFrames = []

    # mappint 对应pose，因为mappint是在某个pose下观测到的
    def set_pose(self, pose):
        self._pose = pose
        
    def set_descriptor(self, descriptor):
        self._descriptor = descriptor
    
    def add_frame(self, frame):
        self._seeFrames.append(frame)

    
