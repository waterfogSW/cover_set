import numpy as np
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from Cover_set_test import cover_set_test

def parse_csv(path : str):
    scp_df = pd.read_csv(path)
    scp_df = scp_df.rename(columns={'X0':'X'})
    scp_df = scp_df.rename(columns={'X1':'Y'})
    return scp_df

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

def clustering(start, end, path):
    df = parse_csv(path)

    # normalize data
    loc = df.values
    sc = StandardScaler()
    sc.fit(loc)
    loc = sc.transform(loc)

    cluster_num = 3
    P = kmeans(loc,cluster_num)

    assert len(df) == len(P)
    # denormalize data
    loc = sc.inverse_transform(loc)
    plt.subplots(figsize=(8, 8))
    plt.scatter(loc[:,0],loc[:,1],c=P)
    plt.show()
    plt.savefig('./result/scatter.png')

    cluster = pd.DataFrame(P, columns = ['cluster'])
    df['cluster'] = cluster

    groups = df.groupby(df.cluster)
    df_arr = []
    for i in range(0, cluster_num):
        df_arr.append(groups.get_group(i))
    
    cover_set_test(start,end,path, P=P)
