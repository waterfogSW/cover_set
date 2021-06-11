import os

from Cover_set_test import cover_set_test

cover_set_test(3,15,"scp_data.csv")
os.system("chmod +x clear.sh")
os.system("./count.sh")
