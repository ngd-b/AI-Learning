"""
task: 通过分析真实的泰坦尼克号的存活数据.预测测试数据里的人员的存活情况

本次采用人工分析数据的方式, 分析数据并给出预测结果

字段释义:
  survival - 存活情况: 0-死亡; 1-存活
  sex      - 性别: male/female
  pclass   - 座位等级: 1/2/3
  Age      - 年龄
  sibsp    - 兄弟姐妹
  parch    - 父母和孩子
  ticket   - 船票编号
  fare     - 船票价格
  cabin    - 船舱编号
  embarked - 登船地点 [C: Cherbourg / Q: Queenstown / S: Southampton]
"""
import pandas as pd
import matplotlib.pyplot as plt

# 使用美化样式（内部已有的主题）
plt.style.use("seaborn-v0_8-whitegrid")

# 设置全局字体（必须在 style.use 之后，否则会被覆盖）
plt.rcParams["font.sans-serif"] = ["Heiti TC", "Songti SC", "Arial Unicode MS"]  # mac 中文字体
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.dpi"] = 150

# 读取真实数据
df = pd.read_csv("train.csv")
print(f"数据形状：{df.shape}")
print(f"前5行数据：\n{df.head()}")
print(f"数据描述：\n{df.describe()}")
# 查看缺失值
print(f"数据信息：\n{df.info()}")

# 填充Age缺失值 （用中位数）
df["Age"] = df["Age"].fillna(df["Age"].median())

# 填充Embarked缺失值 （用众数）
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# 删除Cabin列 （缺失太多）
df = df.drop("Cabin", axis=1)

print("\n 数据清洗后：")
print(df.isnull().sum())

# 性别 vs 存活率
fig, axes = plt.subplots(1, 3, figsize=(10, 4))

survival_by_sex = df.groupby("Sex")["Survived"].mean()
survival_by_sex.plot(kind="bar", ax=axes[0],color=["#FF6B6B", "#4ECDC4"])
axes[0].set_title("性别 vs 存活率")
axes[0].set_ylabel("存活率")
axes[0].set_xticklabels(["女性", "男性"],rotation=0)

# 船舱等级 vs 存活率
survival_by_pclass = df.groupby("Pclass")["Survived"].mean()
survival_by_pclass.plot(kind="bar", ax=axes[1],color=["#FF6B6B", "#4ECDC4","#FFE66D"])
axes[1].set_title("船舱等级 vs 存活率")
axes[1].set_ylabel("存活率")
axes[1].set_xlabel("船舱等级")

# 年龄分布 vs 存活
axes[2].hist(df[df["Survived"] == 1]["Age"], bins=20, alpha=0.5, color="#FF6B6B", label="存活")
axes[2].hist(df[df["Survived"] == 0]["Age"], bins=20, alpha=0.5, color="#4ECDC4", label="未存活")
axes[2].set_title("年龄分布 vs 存活")
axes[2].set_xlabel("年龄")
axes[2].legend()

plt.tight_layout()
plt.savefig("titanic_analysis.png",dpi=300,bbox_inches="tight")
plt.show()

# 相关性热力图
fig, ax = plt.subplots(figsize=(10, 8))

numeric_cols = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']]
corr = numeric_cols.corr()
im = ax.imshow(corr, cmap='RdYlGn',vmin=-1, vmax=1)

ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns,rotation=45)
ax.set_yticklabels(corr.columns)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        ax.text(j, i, f"{corr.iloc[i,j]:.2f}", ha="center", va="center")
plt.colorbar(im)
ax.set_title("相关性热力图")

plt.tight_layout()
plt.savefig("titanic_correlation.png",dpi=300,bbox_inches="tight")
plt.show()


print("\n==== 结论 ====")
print(f"1. 女性存活率：{survival_by_sex['female']:.1%}, 男性存活率：{survival_by_sex['male']:.1%}")
print(f"2. 一等舱存活率：{survival_by_pclass[1]:.1%}, 二等舱存活率：{survival_by_pclass[2]:.1%}, 三等舱存活率：{survival_by_pclass[3]:.1%}")
print(f"3. 年龄与存活相关系数：{corr.loc['Age', 'Survived']:.3f}")