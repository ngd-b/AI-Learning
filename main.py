from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split,cross_val_score,StratifiedKFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

import pandas as pd
import matplotlib.pyplot as plt

# 使用美化样式，内部已有的主题
plt.style.use("seaborn-v0_8-whitegrid")

# 设置全局字体
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]  # mac
plt.rcParams["axes.unicode_minus"] = False

# 提高图形质量
# plt.rcParams["figure.dpi"] = 300


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

# 相关性分析
corr = df.corr()
print(corr["Survived"].sort_values(ascending=False))

# 训练随机森林模型
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)
importance = pd.Series(model.feature_importances_, index=X.columns)
print(importance.sort_values(ascending=False))

# 模型评估
train_score = model.score(X_train_scaled, y_train)
test_score = model.score(X_test_scaled, y_test)

print(f"训练集准确率：{train_score:.3f}")
print(f"测试集准确率：{test_score:.3f}")

# 发现过拟合：训练 0.987，测试 0.816，差距大
# 降低 C 值，加强正则化
model = LogisticRegression(C=0.1, max_iter=1000)  
model.fit(X_train_scaled, y_train)
print(f"训练：{model.score(X_train_scaled, y_train):.3f}")  
print(f"测试：{model.score(X_test_scaled, y_test):.3f}") 

# 交叉验证评估模型稳定性
model = RandomForestClassifier()
scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring="accuracy")

print(f"5折交叉验证：{scores}")
print(f"平均准确率：{scores.mean():.3f} ± {scores.std():.3f}")

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X_train_scaled, y_train, cv=skf)
print(f"5折交叉验证：{scores}")
print(f"平均准确率：{scores.mean():.3f} ± {scores.std():.3f}")

# 交叉验证只是评估模型稳定性，不会训练最终模型
# 需要在完整训练集上重新 fit，才能预测测试集
model.fit(X_train_scaled, y_train)

# 预测测试集
y_pred = model.predict(X_test_scaled)

# 基础指标
print(f"准确率（Accuracy）：{accuracy_score(y_test, y_pred):.3f}")
print(f"精确率（Precision）：{precision_score(y_test, y_pred):.3f}")
print(f"召回率（Recall）：{recall_score(y_test, y_pred):.3f}")
print(f"F1 分数：{f1_score(y_test, y_pred):.3f}")

# 完整报告
print(classification_report(y_test, y_pred))

# 混淆矩阵
print(confusion_matrix(y_test, y_pred))

# 回归评估指标示例（假设 y_test 和 y_pred 是连续值）
# MSE：均方误差（对大误差惩罚更重）
mse = mean_squared_error(y_test, y_pred)

# MAE：平均绝对误差（更直观）
mae = mean_absolute_error(y_test, y_pred)

# R²：决定系数（越接近1越好）
r2 = r2_score(y_test, y_pred)

print(f"均方误差（MSE）：{mse:.3f}")
print(f"平均绝对误差（MAE）：{mae:.3f}")
print(f"R² 决定系数：{r2:.3f}")

# 线性回归示例
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# 预测
y_pred = model.predict(X_test_scaled)

# 查看系数（每个特征的权重）
print(f"系数：{model.coef_}")
print(f"截距：{model.intercept_}")

# 
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# 预测类别
y_pred = model.predict(X_test_scaled)

# 预测概率
y_prob = model.predict_proba(X_test_scaled)

print(f"预测类别：{y_pred[:5]}")
print(f"预测概率：\n{y_prob[:5]}")

# 决策树分类器
model = DecisionTreeClassifier(max_depth=3)  # 限制深度防止过拟合
model.fit(X_train_scaled, y_train)

# 可视化决策树
fig, ax = plt.subplots(figsize=(15, 8))
tree.plot_tree(model, feature_names=X.columns, class_names=["遇难", "存活"], filled=True)
plt.show()

# fig.savefig("fig.png", dpi=300, bbox_inches="tight", facecolor="white")

# 随机森林分类器
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 特征重要性
importance = pd.Series(model.feature_importances_, index=X.columns)
importance.sort_values(ascending=False).plot(kind="bar")
plt.title("特征重要性")
plt.show()