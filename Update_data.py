# 데이터 갱신(이미 선택된 점들 제거)
def update_data(unionSet, totalCircle,data):
    newTotalCircle = []
    unionSet = set(unionSet)
    
    for idx in range(len(data)):
        tempSet = set(totalCircle[idx][1])
        
        tempSet = tempSet - unionSet
        tempSet = list(tempSet)
        
        _temp = [] 
        _temp.append(totalCircle[idx][0])
        _temp.append(tempSet)
        
        # [Item 30] Consider Generators instead of Returning Lists
        newTotalCircle.append(_temp)
        # append함수를 사용하여 리스트에 내용 추가
        
    return newTotalCircle
