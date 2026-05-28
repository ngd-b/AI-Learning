import matplotlib.pyplot as plt

# 设置全局字体
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]  # mac
plt.rcParams["axes.unicode_minus"] = False

# 提高图形质量
plt.rcParams["figure.dpi"] = 300

# 使用美化样式，内部已有的主题
plt.style.use("seaborn-v0_8-whitegrid")

# 绘制一个折线图
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 2, 3, 4])
plt.show()

# 设置标题
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 2, 3, 4])
ax.set_title("折线图")
plt.show()

# 设置坐标轴标签
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 2, 3, 4])
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()

# 绘制一个柱状图
fig, ax = plt.subplots()
ax.bar([1, 2, 3, 4], [1, 2, 3, 4])
plt.show()

# 绘制一个饼图
fig, ax = plt.subplots()
ax.pie([1, 2, 3, 4], labels=["A", "B", "C", "D"])
plt.show()

# 绘制一个箱线图
fig, ax = plt.subplots()
ax.boxplot([[1, 2, 3, 4], [1, 2, 3, 4]])
plt.show()

# 绘制一个热力图
fig, ax = plt.subplots()
ax.imshow([[2, 3, 4, 5], [1, 2, 3, 4]])
plt.show()

# 绘制一个散点图
fig, ax = plt.subplots()
ax.scatter([1, 2, 3, 4], [1, 2, 3, 4])
plt.show()

# 绘制三条折线图
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [5, 10, 20, 34], label="A")
ax.plot([1, 2, 3, 4], [15, 25, 13, 34], label="B")
ax.plot([1, 2, 3, 4], [11, 12, 13, 24], label="C")

plt.legend()
plt.show()

# 标记数据点
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [5, 10, 20, 34], marker="o", color="#D9A85D")
plt.show()

# 绘制多个子图
fig, axs = plt.subplots(1, 2)
axs[0].plot([1, 2, 3, 4], [5, 10, 20, 34])
axs[1].plot([1, 2, 3, 4], [5, 10, 20, 34])
plt.show()

# 关键点标注
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [5, 10, 20, 34])
ax.annotate(
    "关键点",
    xy=(2, 10),
    xytext=(2, 15),
    arrowprops=dict(facecolor="black", shrink=0.05),
)
plt.show()

# 导出高清图
fig.savefig("fig.png", dpi=300, bbox_inches="tight", facecolor="white")
fig.savefig("fig.svg", dpi=300, bbox_inches="tight")
