import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

df = pd.read_csv("creditcard.csv", encoding="utf-8")

df["Class"].value_counts(normalize=True)

df.info()
# абсолютно все столбцы числовые, пропусков нет

pd.options.display.max_columns = 100

df.head(10)

X = df.drop("Class", axis=1)
y = df["Class"]

print(f"Type of X: {type(X)}\nType of y: {type(y)}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=100)

print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

parameters = [{"n_estimators": [10, 15],
                "max_features": np.arange(3, 5),
                "max_depth": np.arange(4, 7)}]

grid = GridSearchCV(estimator=RandomForestClassifier(random_state=100),
                    param_grid=parameters,
                    scoring="roc_auc",
                    cv=3)

grid.fit(X_train, y_train)

print(grid.best_params_)

y_pred_proba = grid.predict_proba(X_test)[:, 1]

from sklearn.metrics import roc_auc_score

print(roc_auc_score(y_train, grid.predict_proba(X_train)[:, 1]))
print(roc_auc_score(y_test, y_pred_proba))

# при сравнении, получилось что roc_auc на тренировочных данных несколько выше
