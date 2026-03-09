# analysis.py
import pandas as pd

# 读取清洗后的 CSV
df = pd.read_csv('../data/链家上海市在售楼盘数据_clean.csv', encoding='utf-8')

print("数据预览：")
print(df.head())

# 区域均价
area_avg = df.groupby('行政区')['价格'].mean().sort_values(ascending=False)
print("\n各区域均价：")
print(area_avg)

# 户型分布
huxing_dist = df['户型'].value_counts()
print("\n户型分布：")
print(huxing_dist)

# 面积区间统计
bins = [0, 50, 80, 120, 200, 1000]
labels = ['0-50㎡','50-80㎡','80-120㎡','120-200㎡','200+㎡']
df['面积区间'] = pd.cut(df['面积'], bins=bins, labels=labels)
area_range_count = df['面积区间'].value_counts().sort_index()
print("\n面积区间分布：")
print(area_range_count)

# 保存统计结果到 CSV
with pd.ExcelWriter('../data/房价统计结果.xlsx') as writer:
    area_avg.to_frame('均价').to_excel(writer, sheet_name='区域均价')
    huxing_dist.to_frame('数量').to_excel(writer, sheet_name='户型分布')
    area_range_count.to_frame('数量').to_excel(writer, sheet_name='面积区间分布')

print("\n分析结果已保存到 data/房价统计结果.xlsx")