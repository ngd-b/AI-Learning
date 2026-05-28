import numpy as np
import pandas as pd

# 创建 Series
series = pd.Series([1, 2, 3, 4, 5])

print(series)

# 带索引的 Series
series = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(series)

# 创建 Series 通过字典
series = pd.Series({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
print(series)


# 创建 DataFrame
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
print(df)

# 创建带索引
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], index=["a", "b"])
print(df)

# 创建带列索引
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=["a", "b", "c"])
print(df)

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=["A", "B", "C"], columns=["a", "b", "c"]
)

# 底部1行 默认 5行
print(df.tail(1))

# 顶部1行
print(df.head(1))

# 获取行索引
print(df.index)

# 获取列索引
print(df.columns)

# 转位numpy
print(df.to_numpy())

# 获取数据类型
print(df.dtypes)

# 获取数据描述
print(df.describe())

# 按照索引排序
print(df.sort_index(axis=1, ascending=False))

# 按照数据值排序
print(df.sort_values(by="a", ascending=False))

# 取列维度数据
print(df["a"])

# 取行维度数据
print(df.loc["A"])

# 取多个列维度数据
print(df[["a", "b"]])

# 切片数据
print(df[1:3])

# 取第一行第一列
print(df.loc["A", "a"])

# 取多个行多个列数据
print(df.loc[["A", "B"], ["a", "b"]])

# 筛选数据
print(df[df["a"] > 4])

# 筛选数据
print(df[df > 2])

print("------------------------------------")
# 求平均值
print(df.mean())

# 求行平均值
print(df.mean(axis=1))

# 操作每一个值
print(df.transform(lambda x: x * 2))

# 合并
print(pd.concat([df, df]))

# 分组
print(df.groupby("a").mean())

print("------------------------------------")

# reindex
dfr = df.reindex(columns=["a", "b", "c", "d"])
print(dfr)

# 清楚缺失值
dfr.loc["A", "d"] = 10
dfd = dfr.dropna(how="any")
print(dfd)

# 填充缺失值
dff = dfr.fillna(value=99)
print(dff)

print("------------------------------------")

# 导出 CSV 数据
df.to_csv("data.csv")

# 导入 CSV 数据
df = pd.read_csv("data.csv")
print(df)

# 导出 Excel 数据
df.to_excel("data.xlsx")

# 导入 Excel 数据
df = pd.read_excel("data.xlsx")
print(df)
