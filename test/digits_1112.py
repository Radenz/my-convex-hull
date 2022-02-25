import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from myConvexHull import convex_hull, random_color
from myConvexHull.point_utils import X, Y

data = datasets.load_digits()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)

plt.figure(figsize=(10, 6))

plt.title('Pixel [1, 3] vs Pixel [1, 4]')

plt.xlabel(data.feature_names[11])
plt.ylabel(data.feature_names[12])

for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:, [11, 12]].values
    hull = convex_hull(bucket)

    color = random_color()

    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i],
                color=color)

    hull = np.transpose(hull)
    plt.plot(hull[X], hull[Y], color=color)

plt.legend()
plt.show()
