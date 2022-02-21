import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from myConvexHull import convex_hull
from myConvexHull.point_utils import X, Y

data = datasets.load_iris()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)

plt.figure(figsize=(10, 6))

colors = ['b', 'r', 'g']

plt.title('Petal Width vs Petal Length')

plt.xlabel(data.feature_names[2])
plt.ylabel(data.feature_names[3])

for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:, [2, 3]].values
    hull = convex_hull(bucket)

    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])

    hull = np.transpose(hull)
    plt.plot(hull[X], hull[Y], colors[i])

plt.legend()
plt.show()
