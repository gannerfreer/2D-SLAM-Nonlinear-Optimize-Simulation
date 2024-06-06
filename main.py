# coding:utf-8
# create by liuzhenbo 2020/8/16 in nwpu
##-------------------------------------------------------------
######   #              #              #           #
#        #             # #            # #         # #
#        #            #   #          #   #       #   #
######   #           # # # #        #     #     #     #
     #   #          #       #      #       #   #       #
     #   #         #         #    #         # #         #
######   #######  #           #  #           #           #
##---------------------------------------------------------------
import time
import numpy as np

# 我的类
from movemodel import MoveModel
from draw import Draw
from landmark import Landmark
from measure import Measure
from slidewindow_graph import Slidewindow_graph

init_pose = np.array([[12.0], [3.0], [0.0]])
estimate_init_pose = np.array([[12.0], [3.0], [0.0]])
move_model = MoveModel(init_pose)
landmarks = Landmark()
slidewindow_graph = Slidewindow_graph()
draw = Draw(landmarks, slidewindow_graph, move_model)

# 传感器半径
r = 3.0

# 循环计数
n = 0
sum = 100
# 主逻辑（*.*）     
#########################################################
while n != sum:
    measure = Measure(move_model, landmarks, r)
    measure.GetMeasure(n)

    if n == 0:
        # 整个框架就是为了维护这个slidewindow_graph结构
        slidewindow_graph.Initialize(estimate_init_pose, measure)
    else:
        t1 = time.perf_counter()
        slidewindow_graph.Update(measure) 
        t2 = time.perf_counter()
        print("optimize cost:",t2-t1)
    draw.Show_result(r)
    
    move_model.Updatepose()
    n = n + 1

# draw.Save_result()
##############################################################
