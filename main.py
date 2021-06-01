import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets

loc = pd.read_csv('/content/scp_data.csv')

plt.scatter(x,y, alpha=0.5)
plt.title('Location')

plt.show()