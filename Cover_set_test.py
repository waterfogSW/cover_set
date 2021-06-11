from Pre_process import parse_csv
from Make_total_circle import make_total_circle
from Process import processing
from Scatter_circles import scatter_circles
import numpy as np
import timeit

# [Item 24]
def cover_set_test(start, end, path, P=None) :
# 디폴트 값을 지정할 때는 [], {}와 같은 mutable 한 애들은 쓰면 안된다.
# None 을 사용함.
    data = parse_csv(path)
    for radius in range(start, end):
        print ("(Creating a circle with radius %d...)" %radius)

        totalCircle = make_total_circle(radius, data)
        totalSelectedPoint = processing(totalCircle, data)
        scatter_circles(totalSelectedPoint, radius, data, P)

        cost_ratio = 1
        n = len(totalSelectedPoint)
        cost = n*radius*cost_ratio

        print("┌─────────────────────────┐")
        print("│radius : %-4d            │" % radius)
        print("│number of circles : %-4d │" % n)
        print("│cost : %-4d              │" % cost)
        print("└─────────────────────────┘")
        print()
