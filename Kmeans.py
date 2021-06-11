import numpy as np
import pandas as pd
from scipy.spatial import distance

# [Item 26] Define Function Decorators with functools.wraps
# kmean 함수 호출시 배열을 인자로 전달하게 됩니다. 
# 디버깅 시에 배열에 값들이 정확히 들어가는지 확인해 보기 위해서 인자를 모두 출력할 수 있도록
# Decorator를 통해 wrapper함수를 사용하였습니다.
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')
        return result
    return wrapper

# trace
def kmeans(loc, k=3, max_iterations=100):
    '''
    loc: Police office location data
    k: number of clusters
    max_iterations: number of repetitions before clusters are established
    '''

    if isinstance(loc, pd.DataFrame):
        loc = loc.values
    idx = np.random.choice(len(loc), k, replace=False)
    centroids = loc[idx, :]
    P = np.argmin(distance.cdist(loc, centroids, 'euclidean'), axis=1)
    for _ in range(max_iterations):
        centroids = np.vstack([loc[P == i, :].mean(axis=0) for i in range(k)])
        tmp = np.argmin(distance.cdist(loc, centroids, 'euclidean'), axis=1)
        if np.array_equal(P, tmp):
            break
        P = tmp
    return P
