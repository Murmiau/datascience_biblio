import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


%matplotlib inline
%config InlineBackend.figure_format = "svg"

from sklearn.datasets import load_boston
boston = load_boston()

X = pd.DataFrame(boston["data"], columns=boston["feature_names"])
X.head()

Y = pd.DataFrame(boston["target"], columns=["price"])
Y.head()

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.manifold import TSNE

TSNE_NEW = TSNE(n_components=2, learning_rate=250, random_state=42)

X_train_scaled_TSNE_NEW = TSNE_NEW.fit_transform(X_train_scaled)

plt.scatter(X_train_scaled_TSNE_NEW[:, 0], X_train_scaled_TSNE_NEW[:, 1])
plt.show()



from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, max_iter=100, random_state=42)

kmeans.fit(X_train_scaled)

train_labels = kmeans.labels_

plt.scatter(X_train_scaled_TSNE_NEW[:, 0], X_train_scaled_TSNE_NEW[:, 1], c=train_labels)
plt.show()

train_clusters = pd.DataFrame({"cluster":kmeans.labels_, "price": Y_train.price.values, "CRIM": X_train.CRIM.values})

train_clusters.groupby("cluster")["price", "CRIM"].mean()



test_labels = kmeans.predict(X_test_scaled)

test_clusters = pd.DataFrame({"cluster": test_labels, "price": Y_test.price.values, "CRIM": X_test.CRIM.values})

test_clusters.groupby("cluster")["price", "CRIM"].mean()
