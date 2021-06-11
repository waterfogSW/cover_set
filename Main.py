from Cover_set_test import cover_set_test
from Count_line import count_line
from Clustering import clustering
import sys

print("[This Program has %d code length]" %count_line())
# [Item 1]
print("[developed version %s]" %sys.version)
# sys 모듈을 활용하여 파이썬 버전출력

print()
print("Would you want Cluserting the data? [Y/n] ", end='')

# [Item 10] Prevent Repetition with Assignment Expressions
if ((c := input()) == 'n'):
    cover_set_test(2, 15, "./data/scp_data.csv")
else:
    clustering(2, 15, "./data/scp_data.csv")

