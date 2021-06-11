from Cover_set_test import cover_set_test
from Count_line import count_line
from Clustering import *

import sys

print("[This Program has %d code length]" %count_line())
print("[developed version %s]" %sys.version)

print()
print("Would you want Cluserting the data? [Y/n] ", end='')
c = input()

if (c == 'n'):
    cover_set_test(1, 15, "scp_data.csv")
else:
    clustering(1, 15, "scp_data.csv")

