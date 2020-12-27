import pandas as pd
import numpy as np


word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Grape': '포도'
    }

frequency_dict = {
    'Apple': 3,
    'Banana': 6,
    'Carrot': np.nan,
    'Grape': 4
    }

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1,
    'Grape': 5
    }

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
    })

print(summary)
print(summary.notnull())
print(summary.isnull())
#summary['frequency'] = summary['frequency'].fillna('noData')
#print(summary)
summary['frequency'] = summary['frequency'].fillna(0)
print(summary)

summary = summary.sort_values('frequency', ascending=False)
print(summary)