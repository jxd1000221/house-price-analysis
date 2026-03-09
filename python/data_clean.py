# data_clean.py
import pandas as pd

# 读取原始 CSV
df = pd.read_csv('../data/链家上海市在售楼盘数据.csv', encoding='utf-8')

# 查看前几行
print("原始数据预览：")
print(df.head())

# 处理缺失值
df.fillna({'价格': df['价格'].median(), '面积': df['面积'].median()}, inplace=True)

# 处理异常值（简单示例）
df = df[(df['价格'] > 1000) & (df['价格'] < 1000000)]  # 价格在合理范围
df = df[(df['面积'] > 10) & (df['面积'] < 1000)]       # 面积在合理范围

# 统一字段类型
df['价格'] = df['价格'].astype(float)
df['面积'] = df['面积'].astype(float)

# 输出清洗后的 CSV
df.to_csv('../data/链家上海市在售楼盘数据_clean.csv', index=False, encoding='utf-8')
print("数据清洗完成，已保存到 data/ 链家上海市在售楼盘数据_clean.csv")