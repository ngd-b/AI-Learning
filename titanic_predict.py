import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

import matplotlib.pyplot as plt

# 使用美化样式，内部已有的主题
plt.style.use("seaborn-v0_8-whitegrid")

# 设置全局字体
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]  # mac
plt.rcParams["axes.unicode_minus"] = False


df = pd.read_csv("train.csv")

# 特征选择
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
df = df[features + ["Survived"]]

# 缺失值处理
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# 类别编码
df["Sex"] = df["Sex"].map({"female": 0, "male": 1})
df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

X = df.drop("Survived", axis=1)
y = df["Survived"]

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 特征缩放
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 模型1：逻辑回归
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train_scaled, y_train)
lr_score = lr.score(X_test_scaled, y_test)
print(f"\n逻辑回归准确率：{lr_score:.3f}")

# 模型2：随机森林
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)  # 随机森林不需要缩放
rf_score = rf.score(X_test, y_test)
print(f"随机森林准确率：{rf_score:.3f}")

# 交叉验证
lr_cv = cross_val_score(lr, X_train_scaled, y_train, cv=5)
rf_cv = cross_val_score(rf, X_train, y_train, cv=5)

print(f"\n逻辑回归 5折交叉验证：{lr_cv.mean():.3f} ± {lr_cv.std():.3f}")
print(f"随机森林 5折交叉验证：{rf_cv.mean():.3f} ± {rf_cv.std():.3f}")

# 模型评估
best_model = rf 
y_pred = best_model.predict(X_test)

print("\n=== 混淆矩阵 ===")
print(confusion_matrix(y_test, y_pred))

print("\n=== 分类报告 ===")
print(classification_report(y_test, y_pred, target_names=["遇难", "存活"]))

# 绘制特征重要性
importance = pd.Series(best_model.feature_importances_, index=X.columns)
importance.sort_values(ascending=True).plot(kind="barh")
plt.title("特征重要性")
plt.xlabel("重要性")
plt.tight_layout()

# plt.savefig("feature_importance.png",dpi=300, bbox_inches="tight", facecolor="white")
# plt.show()

# 加载测试数据集
test_df = pd.read_csv("test.csv")
passenger_ids = test_df["PassengerId"]

# 用同样的特征
test_df = test_df[features]

# 清洗数据
test_df["Age"] = test_df["Age"].fillna(test_df["Age"].median())
test_df["Fare"] = test_df["Fare"].fillna(test_df["Fare"].median())
test_df["Embarked"] = test_df["Embarked"].fillna(test_df["Embarked"].mode()[0])

# 类别编码
test_df["Sex"] = test_df["Sex"].map({"female": 0, "male": 1})
test_df = pd.get_dummies(test_df, columns=["Embarked"], drop_first=True)


# 预测
predictions = best_model.predict(test_df)

# 生成提交文件
submission = pd.DataFrame({
    "PassengerId": passenger_ids,
    "Survived": predictions
})
submission.to_csv("submission.csv", index=False)
print("提交文件已生成！")


# 优化 - 模型调参
# 定义参数网格
params = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 10, None],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
}

# 网格搜索
grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    params,
    cv=5,
    scoring="accuracy",
    n_jobs=-1  # 用所有 CPU 核心，加快速度
)

grid.fit(X_train, y_train)

print(f"最优参数：{grid.best_params_}")
print(f"最优分数：{grid.best_score_:.3f}")

best_rf = grid.best_estimator_
predictions = best_rf.predict(test_df)

# 生成提交文件
submission = pd.DataFrame({
    "PassengerId": passenger_ids,
    "Survived": predictions
})
submission.to_csv("submission_optimized.csv", index=False)
print("提交文件已生成！")