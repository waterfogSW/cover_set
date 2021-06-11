import os

from Cover_set_test import cover_set_test

os.system("chmod +x count.sh")
os.system("./count.sh")

cover_set_test(3,15,"scp_data.csv")

