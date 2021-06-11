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
    radius = range(start, end)
    # [Item 27] 
    # [Item 28]
    area =  [r**2 for r in radius]
    # map 대신 Comprehensions 사용. 
    # Comprehension을 사용할 때에는 두 개 이상의 복잡한 연산을 수행하지 않는다.

    # [Item 6] Prefer Multiple Assignment Unapcking Over Indexing
    for i,r in enumerate(radius):
        print ("(%d: Creating a circle with radius %d...)" %(i, r))

        totalCircle = make_total_circle(r, data)
        totalSelectedPoint = processing(totalCircle, data)
        scatter_circles(totalSelectedPoint, r, data, cluster_data)

        n = len(totalSelectedPoint)
        total_area = (area[i]**2)*n

        print("┌──────────────────────────────┐")
        print("│radius: %-6d                │" % r)
        print("│number of circles: %-6d     │" % n)
        print("│total area: %-6d            │" % total_area)
        print("└──────────────────────────────┘")
        print()
