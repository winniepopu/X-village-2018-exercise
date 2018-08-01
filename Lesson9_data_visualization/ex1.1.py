## ex1 使用panda印出
# 數學分數平均值 - - - (上面填空值時有用到平均值計算方法)
# 數學分數總和 - - - (A班平均多少，總分多少，B班平均...)
# 數學分數與英文分數的相關係數

import pandas as pd
table = [
    ['A', 'Noah', 90, 92],
    ['B', 'Liam', 81, 83],
    ['C', 'William', 87,85],
    ['B', 'Benjamin.', 82,80],
    ['A', 'Emma.', 90,94],
    ['C', 'Olivia', 50,60],
    ['A', 'Isabella', 70,71],
    ['C', 'Amelia', 84,86],
    ['B', 'Mia', 88,85],
]
df = pd.DataFrame(table,columns = ['class', 'name', 'math_score', 'eng_score'])

print(df['math_score'].mean())
print(df['eng_score'].sum())

print(df.groupby('class').sum())
print(df.groupby('class').mean())

print(df.corr())