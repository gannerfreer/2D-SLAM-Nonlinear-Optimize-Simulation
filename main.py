# coding:utf-8
# create by liuzhenbo 2020/8/16 in nwpu
# modified by gray 2024/6/7 in hnu
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

measure = Measure(move_model, landmarks, r)
# measure.SerializeMeasure(100)
f = measure.DeserializeMeasure()

# 循环计数
step = 0
end = f
# 主逻辑（*.*）     
#########################################################
while step != end:
    measure = Measure(move_model, landmarks, r)
    measure.GetMeasure(step)

    if step == 0:
        # 整个框架就是为了维护这个slidewindow_graph结构
        slidewindow_graph.Initialize(estimate_init_pose, measure)
    else:
        t1 = time.perf_counter()
        slidewindow_graph.Update(measure) 
        t2 = time.perf_counter()
        print("optimize cost:",t2-t1)
    draw.Show_result(r)
    
    move_model.Updatepose()
    step = step + 1

# draw.Save_result()
##############################################################
