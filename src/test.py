import pandas as pd

# 创建一个示例DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# 获取DataFrame的行名
row_names = df.index
row_names = df.index.values
print(row_names)
