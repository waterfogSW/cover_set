from Make_circle import make_circle

def make_total_circle(radius, data):
    totalCircle = []
    totalCircleSize = []
    for idx in range(data['X'].size):
        ax = data.values[idx][0]
        ay = data.values[idx][1]
    
        _circle, _circleSize = make_circle(ax, ay, data, radius)
        totalCircle.append(_circle)
        totalCircleSize.append(_circleSize)
    
    return totalCircle