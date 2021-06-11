from Pre_process import parse_csv
from Make_total_circle import make_total_circle
from Process import processing
from Scatter_circles import scatter_circles
import numpy as np
import timeit

# [Item 23] Provide Optional Behavior with Keyword Arguments
# 3번째 인자에 P=np.array([])와 같이 Keyword argument를 지정하여 
# 함수 사용시에 인자로 어떤 값이 들어가야 하는지 직관적으로 이해할 수 있도록 하였습니다.
def cover_set_test(start, end, path, cluster_data=np.array([])) :
    data = parse_csv(path)
    for radius in range(start, end):
        print ("(Creating a circle with radius %d...)" %radius)

        totalCircle = make_total_circle(radius, data)
        totalSelectedPoint = processing(totalCircle, data)
        scatter_circles(totalSelectedPoint, radius, data, cluster_data)

        cost_ratio = 1
        n = len(totalSelectedPoint)
        cost = n*radius*cost_ratio

        print("┌─────────────────────────┐")
        print("│radius : %-4d            │" % radius)
        print("│number of circles : %-4d │" % n)
        print("│cost : %-4d              │" % cost)
        print("└─────────────────────────┘")
        print()
