from Pre_process import parse_csv
from Make_total_circle import make_total_circle
from Process import processing
from Scatter_circles import scatter_circles
import numpy as np
import timeit

# [Item 24] Use None and Docstrings to Specify Dynamic Default Arguments
def cover_set_test(start, end, path, P=None) :
    data = parse_csv(path)
    radius = range(start, end)
    # [Item 27]
    # [Item 28]
    area =  [r**2 for r in radius]
    # map 대신 Comprehensions 사용. 
    # Comprehension을 사용할 때에는 두 개 이상의 복잡한 연산을 수행하지 않는다.

    # [Item 6] Prefer Multiple Assignment Unapcking Over Indexing
    # [Item 7] Prefer enumerate Over range
    for i,r in enumerate(radius):
        print ("(%d: Creating a circle with radius %d...)" %(i, r))

        totalCircle = make_total_circle(r, data)
        totalSelectedPoint = processing(totalCircle, data)
        scatter_circles(totalSelectedPoint, r, data, P)

        n = len(totalSelectedPoint)
        total_area = (area[i]**2)*n

        print("┌──────────────────────────────┐")
        print("│radius: %-6d                │" % r)
        print("│number of circles: %-6d     │" % n)
        print("│total area: %-6d            │" % total_area)
        print("└──────────────────────────────┘")
        print()
