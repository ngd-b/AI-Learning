""""""

task: 通过分析真实的泰坦尼克号的存活数据.预测测试数据里的人员的存活情况

本次采用人工分析数据的方式, 分析数据并给出预测结果
字段释义
survival-存活情况:0-死亡;1-存活
sex-性别:male/female
pclass-座位等级:1/2/3
Age
sibsp-兄弟姐妹
parch-父母和孩子
ticket-船票编号
fare-船票价格
cabin-船舱编号
embarked-登船地点[C:Cherbourg/Q:Queenstown:S/Southampton]
""
import pandas as pd
import matplotlib.pyplot as plt

# 设置全局字体
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]  # mac
plt.rcParams["axes.unicode_minus"] = False

# 提高图形质量
plt.rcParams["figure.dpi"] = 300

# 使用美化样式，内部已有的主题
plt.style.use("seaborn-v0_8-whitegrid")

# 读取真实数据
df = pd.read_csv("train.csv")
print(df.head())

# 加载测试数据
df_test = pd.read_csv("test.csv")
print(df_test.head())

# 统计女性的存活数量、存活率
female_survived = df.loc[df["Sex"] == "female"]["Survived"]
female_survived_rate = sum(female_survived) / len(female_survived)
print(f"女性存活率：{female_survived_rate:.2%}")

# 统计男性的存活数量、存活率
male_survived = df.loc[df["Sex"] == "male"]["Survived"]
male_survived_rate = sum(male_survived) / len(male_survived)
print(f"男性存活率：{male_survived_rate:.2%}")
