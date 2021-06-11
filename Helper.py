from Cover_set_test import cover_set_test
from Clustering import clustering

def helper(c):
    if (c == 'n'):
        cover_set_test(2, 15, "./data/scp_data.csv")
    else:
        clustering(2, 15, "./data/scp_data.csv")