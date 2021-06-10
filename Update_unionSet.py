# 합집합 갱신 
def update_unionSet(totalSelectedPoint, unionSet, selectedPoint):
    totalSelectedPoint.append(selectedPoint[0])
    unionSet += selectedPoint[1]
    
    return totalSelectedPoint, unionSet