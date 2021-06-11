from Cover_set_test import cover_set_test
from Clustering import clustering

def helper():
    # [Item 10] Prevent Repetition with Assignment Expressions
    if ((c := input()) == 'n'):
        cover_set_test(2, 15, "./data/scp_data.csv")
    else:
        clustering(2, 15, "./data/scp_data.csv")