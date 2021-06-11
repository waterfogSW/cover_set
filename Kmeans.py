import numpy as np
import pandas as pd
from scipy.spatial import distance

def kmeans(loc,k=3,max_iterations=100):
    '''
    loc: Police office location data
    k: number of clusters
    max_iterations: number of repetitions before clusters are established
    '''
    if isinstance(loc, pd.DataFrame):loc = loc.values
    idx = np.random.choice(len(loc), k, replace=False)
    centroids = loc[idx, :]
    P = np.argmin(distance.cdist(loc, centroids, 'euclidean'),axis=1)
    for _ in range(max_iterations):
        centroids = np.vstack([loc[P==i,:].mean(axis=0) for i in range(k)])
        tmp = np.argmin(distance.cdist(loc, centroids, 'euclidean'),axis=1)
        if np.array_equal(P,tmp):break
        P = tmp
    return P