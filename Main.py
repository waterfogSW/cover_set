from Count_line import count_line
from Helper import helper
import sys

print("[This Program has %d code length]" %count_line())
# [Item 1]
print("[developed version %s]" %sys.version)
# sys 모듈을 활용하여 파이썬 버전출력

print()
print("Would you want Cluserting the data? [Y/n] ", end='')
c = input()
helper(c)


