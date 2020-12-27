import pandas as pd

array = pd.Series(['사과','바나나','당근'],index=[1,2,3])

print(array[1])

word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근'
    }

frequency_dict = {
    'Apple': 3,
    'Banana': 6,
    'Carrot': 8
    }

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1
    }


word = pd.Series(word_dict)
freq = pd.Series(frequency_dict)
imprtance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': freq,
    'importance': importance_dict
    })

score = summary['frequency'] * summary['importance']

summary['score'] = score

print(summary)

#DF slicing by name
print(summary.loc['Banana':'Carrot','importance':])
#slicing by index
print(summary.iloc[1:3,2:])
#Data change by name
summary.loc['Apple','importance'] = 5
#New data insert
summary.loc['Grape'] = ['포도',4 ,7, 28]
print(summary)

#save
summary.to_csv("summary.csv", encoding='utf-8-sig')
saved = pd.read_csv("summary.csv", index_col=0)
print(saved)

