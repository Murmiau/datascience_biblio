import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from pylab import rcParams

plt.style.use("fivethirtyeight")

df = pd.read_csv("creditcard.csv")
df.head()

df["Class"].value_counts()

rcParams["figure.figsize"] = 5, 5
df["Class"].value_counts().plot(kind="bar")

rcParams["figure.figsize"] = 5, 5
df["Class"].value_counts().plot(kind="bar", logy=True)

fig, ax = plt.subplots(nrows=1, ncols=2)

ax1, ax2 = ax.flatten()

ax1.hist(df[df["Class"] == 0]["V1"], density=True, bins=20, alpha=0.5, color="grey", label="Class 0")
ax1.set_xlabel("Class")
ax2.hist(df[df["Class"] == 1]["V1"], density=True, bins=20, alpha=0.5, color="red", label="Class 1")
ax2.set_xlabel("Class")

fig.legend(loc="upper center")

fig.set_size_inches(10, 5)

plt.subplots_adjust(wspace=0.3)
