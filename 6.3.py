import pandas as pd
import numpy as np

?RandomForestRegressor

# feature_importances_ : array of shape = [n_features]
# The feature importances (the higher, the more important the feature).

print("Сумма всех показателей важности:", np.round(np.sum(model.feature_importances_)))

feature_dict = {}
for feature, importance in zip(boston.feature_names, model.feature_importances_):
    feature_dict[feature] = importance
    print(feature, ':', np.round(importance, 4))

sorted(feature_dict.items(), key=lambda kv: kv[1], reverse=True)[:2]

# 2 признака, показывающие наибольшую важность - LSTAT и RM
