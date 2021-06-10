import math

def isInCircle(Cx, Cy, Px, Py, radius : int):
    dist = math.sqrt((Cx-Px)**2 + (Cy-Py)**2)
    if dist <= radius:
        return True
    else:
        return False