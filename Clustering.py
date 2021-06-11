import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from Cover_set_test import cover_set_test
from Pre_process import parse_csv
from Kmeans import kmeans
from Mkdir import createFolder 

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
    createFolder("result")

    # Linux shell에서는 plt.show()의 GUI를 지원하지 않아 result폴더에 따로 결과를 저장함.
    plt.savefig('./result/scatter.png')

    cluster = pd.DataFrame(P, columns = ['cluster'])
    df['cluster'] = cluster

    groups = df.groupby(df.cluster)
    df_arr = []
    for i in range(0, cluster_num):
        df_arr.append(groups.get_group(i))
    
    cover_set_test(start,end,path, P=P)

