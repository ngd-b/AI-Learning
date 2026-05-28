import numpy as np

# 创建一个数组
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 创建一个二维数组
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 创建用0填充的数组
arr = np.zeros((3, 3))
print(arr)

# 创建用1填充的数组
arr = np.ones((3, 3))
print(arr)

# 创建空数组，空数组内部会用随机数填充元素
arr = np.empty((3, 3))
print(arr)

# 创建一个范围数组
arr = np.arange(0, 10, 2)
print(arr)

# 创建一个线性分布数组
arr = np.linspace(0, 10, 5)
print(arr)

arr = np.array(
    [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]]
)

# 获取数组的维度
print(arr.ndim)

# 获取数组的形状
print(arr.shape)

# 获取数组有多少元素
print(arr.size)

arr = np.array([[1, 2, 3], [4, 5, 6]])

# 将数组重构为 1D
print(arr.ravel())

# 将数组重构为 2D
print(arr.reshape(3, 2))

# 将数组重构为 3D
print(arr.reshape(1, 2, 3))

arr = np.array([1, 2, 3])

# 扩展行
print(arr[np.newaxis, :])

# 扩展列
print(arr[:, np.newaxis])

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(np.expand_dims(arr, axis=1))

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

# 乘法
print(arr1 * 2)

# 减法
print(arr1 - 2)

# 求和
print(arr1.sum())

# 按行求和
print(arr1.sum(axis=0))

# 按列求和
print(arr1.sum(axis=1))

arr = np.array([[1, 2, 3], [4, 5, 6]])

# 切片
print(arr[1:])

# 筛选
print(arr[arr > 3])
