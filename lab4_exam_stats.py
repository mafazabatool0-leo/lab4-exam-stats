import pandas as pd
import numpy as np
from scipy import stats

scores = pd.Series([
    72, 65, 88, np.nan, 54,
    91, 76, np.nan, 83, 69
])

print("Descriptive Statistics:")
print(scores.describe())

valid_scores = scores.dropna()

print("\nSkewness:", stats.skew(valid_scores))
print("Kurtosis:", stats.kurtosis(valid_scores))

print("\nMissing values:", scores.isnull().sum())

mean_score = scores.mean()

filled_scores = scores.fillna(mean_score)

print("\nFilled scores:")
print(filled_scores)