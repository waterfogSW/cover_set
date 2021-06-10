# 데이터 갱신(이미 선택된 점들 제거)
def update_data(unionSet, totalCircle):
    newTotalCircle = []
    unionSet = set(unionSet)
    
    for idx in range(500):
        tempSet = set(totalCircle[idx][1])
        
        tempSet = tempSet - unionSet
        tempSet = list(tempSet)
        
        _temp = [] 
        _temp.append(totalCircle[idx][0])
        _temp.append(tempSet)
        
        newTotalCircle.append(_temp)
        
    return newTotalCircle