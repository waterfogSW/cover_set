from Pre_process import parse_csv
from Make_total_circle import make_total_circle
from Process import processing
from Scatter_circles import scatter_circles

def cover_set_test(start, end, path) :
    for radius in range(start, end):
        data = parse_csv(path)
        totalCircle = make_total_circle(radius, data)
        totalSelectedPoint = processing(totalCircle)
        print ("반지름 길이: {radius}인 원 생성, 선택된 점들".format(radius=radius))
        print(totalSelectedPoint)

        scatter_circles(totalSelectedPoint, radius, data)
        print("선택된 원의 갯수: {num}".format(num=len(totalSelectedPoint)))
        print("\n\n")