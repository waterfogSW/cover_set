import math
# 유클리드 거리 계산 메서드
def isInCircle(ax, ay, bx, by, radius):
    _len = math.sqrt((ax-bx)**2 + (ay-by)**2) 
    if _len <= radius:
        return True
    else:
        return False