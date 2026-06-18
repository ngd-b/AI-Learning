from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

# 读取真实数据
df = pd.read_csv("train.csv")
print(f"数据形状：{df.shape}")
print(df.head())
print(df.describe())
# 查看缺失值
print(df.info())

# 填充Age缺失值 （用中位数）
df["Age"] = df["Age"].fillna(df["Age"].median())

# 填充Embarked缺失值 （用众数）
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# 删除Cabin列 （缺失太多）
df = df.drop("Cabin", axis=1)

# 删除对预测无用的列
df = df.drop(columns=["PassengerId", "Name", "Ticket"])

# 对分类特征做独热编码
df = pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True)

print("\n 数据清洗后：")
print(df.isnull().sum())
print(f"\n 特征列：{list(df.columns)}")


# 标签 y 比如年龄、性别等，除了特征之外的
X = df.drop(columns=["Survived"])
# 特征 X 就是是否存活
y = df["Survived"]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42,stratify=y
)

# 划分训练集和验证集
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.25, random_state=42,stratify=y_train
)

print(f"训练集大小：{X_train.shape[0]}")
print(f"验证集大小：{X_val.shape[0]}")
print(f"测试集大小：{X_test.shape[0]}") 

# ========== 缩放方式对比 ==========

# 方式1: StandardScaler（Z-score 标准化）— 均值为0，标准差为1
standard_scaler = StandardScaler()
X_train_standard = standard_scaler.fit_transform(X_train)
X_val_standard = standard_scaler.transform(X_val)
X_test_standard = standard_scaler.transform(X_test)

print(f"\n[StandardScaler] 训练集均值: {X_train_standard.mean(axis=0).round(2)}")
print(f"[StandardScaler] 训练集标准差: {X_train_standard.std(axis=0).round(2)}")

# 方式2: MinMaxScaler（归一化）— 缩放到 [0, 1] 区间
minmax_scaler = MinMaxScaler()
X_train_minmax = minmax_scaler.fit_transform(X_train)
X_val_minmax = minmax_scaler.transform(X_val)
X_test_minmax = minmax_scaler.transform(X_test)

print(f"\n[MinMaxScaler] 训练集最小值: {X_train_minmax.min(axis=0).round(2)}")
print(f"[MinMaxScaler] 训练集最大值: {X_train_minmax.max(axis=0).round(2)}")

# 后续建模时选择一种即可，这里默认使用 StandardScaler
X_train_scaled = X_train_standard
X_val_scaled = X_val_standard
X_test_scaled = X_test_standard

