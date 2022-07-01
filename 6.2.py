import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=1000, max_depth=12, random_state=42)

model.fit(X_train, y_train.values[:, 0])

y_pred_rf = model.predict(X_test)

print(r2_score(y_test, y_pred_rf))

# RandomForest работает лучше, чем линейная регрессия
# Результат r2 на отложенной выборке: 0.87 // 0.71
