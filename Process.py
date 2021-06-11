from Update_unionSet import update_unionSet
from Update_data import update_data

# 최적의 중심점들을 도출
def processing(totalCircle, data):
    unionSet = []
    totalSelectedPoint = []
    
    while len(unionSet) < len(data):
        # sort
        totalCircle.sort(key = lambda x:len(x[1]), reverse=True)
        
        # 가장 큰 집합 선택
        selectedPoint = totalCircle[0]
        
        # 좌표 append, 합집합 갱신
        totalSelectedPoint, unionSet = update_unionSet(totalSelectedPoint, unionSet, selectedPoint)
        
        # 처음 좌표의 리스트 기준으로 나머지 리스트 갱신
        totalCircle = update_data(unionSet, totalCircle, data)
        
        
    return totalSelectedPoint
