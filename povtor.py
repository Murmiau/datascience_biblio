import pandas as pd
import numpy as np

from sklearn.datasets import load_wine

data = load_wine()


print(type(data))

data_keys = data.keys()
print(data_keys)


print(data["data"].shape)

print(data["feature_names"])

print(data["DESCR"])


print(np.unique(data["target"]))
# целевая переменная содержит 3 класса

print(data["target_names"])


X = pd.DataFrame(data["data"], columns=data["feature_names"])

print(type(X))

X.head()


print(X.shape)

print(X.info())

print(X.isna().any())
# пропущенных значений нет


X["target"] = np.int64(data["target"])

X["target"].value_counts()

print(type(X["target"].values[0]))


X_corr = X.corr()

X_corr.head()


high_corr = list(X_corr["target"][:-1][X_corr["target"][:-1] > np.abs(0.5)].index)

print(high_corr)

X.drop("target", axis=1, inplace=True)

for feature in high_corr:
    X[str(feature) + '2'] = X[feature] ** 2

X.columns

X.describe()
