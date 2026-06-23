import torch
import numpy as np
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import classification_report

# 基础创建
t = torch.tensor([1,2,3,4,5])
print(t)
print(t.dtype)

# 指定类型
t = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
print(t.dtype) 

# 创建全 0 / 全 1
t = torch.zeros(3, 3)
print(t)
t = torch.ones(3, 3)
print(t)

# 随机数
t = torch.rand(3, 3)      # 0-1 均匀分布
print(t)
t = torch.randn(3, 3)     # 标准正态分布
print(t)

# 创建范围
t = torch.arange(0, 10, 2)
print(t)

a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

# 基本运算
print(a + b)      # tensor([5., 7., 9.])
print(a * b)      # tensor([4., 10., 18.])
print(a @ b)      # tensor(32.)  点积

# 形状操作
t = torch.rand(2, 3)
print(t.shape)          # torch.Size([2, 3])
print(t.reshape(3, 2))  # 重构为 3x2
print(t.T)              # 转置

# NumPy → Tensor
arr = np.array([1, 2, 3])
t = torch.from_numpy(arr)
print(arr,t)

# Tensor → NumPy
arr = t.numpy()
print(arr)

# 自动选择可用设备
if torch.cuda.is_available():
    # NVIDIA GPU / Linux/ Windows
    device = "cuda"
elif torch.backends.mps.is_available():
    # Apple GPU M1 / M2 / M2 / M3
    device = "mps"
else:
    device = "cpu"

print(f"Using device: {device}")

t = torch.tensor([1, 2, 3])
t_gpu = t.to(device)        
t_cpu = t_gpu.to("cpu")  

# 创建一个 tensor，开启梯度追踪
x = torch.tensor(2.0, requires_grad=True)

# 前向计算
y = x ** 2 + 3 * x + 1  # y = x² + 3x + 1

# 反向传播：计算 dy/dx 变化率
y.backward()

# 梯度 = dy/dx = 2x + 3 = 2*2 + 3 = 7
print(x.grad) 

# 1. 固定轮数，就跑十次
x = torch.tensor(2.0, requires_grad=True)

for i in range(10):
    y = x ** 2 + 3 * x + 1
    y.backward()
    with torch.no_grad():
        x -= 0.1 * x.grad
        x.grad.zero_()
        
y = x ** 2 + 3 * x + 1
y.backward()
print(x.grad)

x = torch.tensor(2.0, requires_grad=True)

prev_loss = float("inf")
while True:
    y = x ** 2 + 3 * x + 1
    loss = y.item()

    if abs(prev_loss - loss)/prev_loss < 0.001:
        print(f"损失不再下降，停止训练")
        break
    prev_loss = loss
    y.backward()
    with torch.no_grad():
        x -= 0.1 * x.grad
        x.grad.zero_()

y = x ** 2 + 3 * x + 1
y.backward()
print(x.grad) 

# 3. 早停
x = torch.tensor(2.0, requires_grad=True)

best_loss = float("inf")
patience = 10  # 连续10 轮没改善就停
counter = 0

for i in range(1000):
    y = x ** 2 + 3 * x + 1
    loss = y.item()
    if loss < best_loss - 0.001: # 改善超过0.001，更新参数
        best_loss = loss
        counter = 0
    else:
        counter += 1
        if counter >= patience:
            print(f"连续{patience} 轮没改善，停止训练")
            break

    y.backward()
    with torch.no_grad():
        x -= 0.1 * x.grad
        x.grad.zero_()
        
y = x ** 2 + 3 * x + 1
y.backward()
print(x.grad) 


# SGD - 随机梯度下降
x = torch.tensor(2.0, requires_grad=True)

# SGD - 随机梯度下降
#optimizer = torch.optim.SGD([x], lr=0.1)
# Adam - 自适应学习率优化器
optimizer = torch.optim.Adam([x], lr=0.1)

best_loss = float("inf")
patience = 50  # 连续10 轮没改善就停
counter = 0

for i in range(1000):
    y = x ** 2 + 3 * x + 1
    loss = y.item()
    if loss < best_loss - 0.001: # 改善超过0.001，更新参数
        best_loss = loss
        counter = 0
    else:
        counter += 1
        if counter >= patience:
            print(f"连续{patience} 轮没改善，停止训练")
            break

    optimizer.zero_grad()
    y.backward()
    optimizer.step()
    
y = x ** 2 + 3 * x + 1
y.backward()
print(x.grad) 

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        # 定义层
        self.fc1 = nn.Linear(10, 64)   # 输入 10，输出 64
        self.fc2 = nn.Linear(64, 32)   # 输入 64，输出 32
        self.fc3 = nn.Linear(32, 1)    # 输入 32，输出 1

    def forward(self, x):
        # 定义数据流
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x

# 创建模型
model = SimpleNet()
# 使用模型
x = torch.randn(10)
y = model(x)

# 输出模型结构
print(model)
print(x,y)
# 查看模型参数
for name, param in model.named_parameters():
    print(name, param.shape)

# ReLU
relu = nn.ReLU()
print(relu(torch.tensor([-1.0, 0.0, 1.0])))  

# Sigmoid
sigmoid = nn.Sigmoid()
print(sigmoid(torch.tensor([0.0])))  

# Softmax
softmax = nn.Softmax(dim=0)
print(softmax(torch.tensor([1.0, 2.0, 3.0]))) 

# Tanh
tanh = nn.Tanh()
print(tanh(torch.tensor([0.0])))

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        # 定义层
        self.fc1 = nn.Linear(10, 64)   # 输入 10，输出 64
        self.fc2 = nn.Linear(64, 32)   # 输入 64，输出 32
        self.fc3 = nn.Linear(32, 1)    # 输入 32，输出 1
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # 定义数据流
        x = self.relu(self.fc1(x)) 
        x = self.relu(self.fc2(x))
        x = self.sigmoid(self.fc3(x))
        return x

# 创建模型
model = SimpleNet()

x = torch.randn(10)
print(model(x))

# MSE
mse = nn.MSELoss()
loss = mse(torch.tensor([1.0, 2.0]), torch.tensor([1.5, 2.5]))
print(loss)  

# 二分类
bce = nn.BCELoss()
loss = bce(torch.tensor([0.9, 0.1]), torch.tensor([1., 0.]))
print(loss)

# 多分类
ce = nn.CrossEntropyLoss()
loss = ce(torch.tensor([[0.1, 0.9], [0.8, 0.2]]),  
          torch.tensor([1, 0]))                    
print(loss)

# 损失函数
criterion = nn.BCELoss()  # 二分类用 BCELoss

# 准备数据
X = torch.randn(5, 10)              # 5 个样本，10 个特征
y = torch.tensor([1., 0., 1., 0., 1.])  # 真实标签

# 前向计算
output = model(X)                    # 输出 5 个概率值
print(f"预测：{output.squeeze()}")
print(f"真实：{y}")

# 计算损失
loss = criterion(output.squeeze(), y)
print(f"损失：{loss.item():.4f}") 

# 创建数据集
X = torch.randn(100, 10)
y = torch.randn(100, 1)
dataset = TensorDataset(X, y)

# 创建 DataLoader： batch_size - 批次大小， shuffle - 是否打乱数据
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

# 遍历
for batch_X, batch_y in dataloader:
    print(batch_X.shape)  
    print(batch_y.shape) 
    break
    
    
# 200 个样本，5 个特征
X = torch.randn(200, 5)
# 定义标签，根据每个样本的前两个值确定标签
y = (X[:, 0] + X[:, 1] > 0).float().unsqueeze(1)  

# 创建数据集
dataset = TensorDataset(X, y)
# 创建数据加载器：批次大小为 32，随机打乱
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# 创建模型: 按顺序执行
model = nn.Sequential(
  nn.Linear(5, 16),
  nn.ReLU(),
  nn.Linear(16, 1),
  nn.Sigmoid()
)

# 根据 y 标签判断任务是一个二分类任务
criterion = nn.BCELoss()
# 优化器
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

best_loss = float('inf')
patience = 10
counter = 0

for epoch in range(1000):
    total_loss = 0
    for batch_X,batch_y in dataloader:
        y_pred = model(batch_X)
        loss = criterion(y_pred, batch_y)

        # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(dataloader)
    if avg_loss < best_loss:
        best_loss = avg_loss
        counter = 0
    else:
        counter += 1
        if counter >= patience:
            break
        
# 评估模型
test_X = torch.randn(20, 5)
test_y = (test_X[:, 0] + test_X[:, 1] > 0).float().unsqueeze(1)  

model.eval()
with torch.no_grad():
    test_pred = model(test_X)

    # 二分类
    predicted = (test_pred > 0.5).float()
    accuracy = (predicted == test_y).float().mean()
    print(f'Accuracy: {accuracy.item():.4f}')

    # 混淆矩阵
    print(classification_report(test_y.numpy(), predicted.numpy()))
    
# 32x32 灰度图像
# 1张，1通道，32x32
x = torch.randn(1, 1, 32, 32)

# 1 输入通道，16输出通道，卷积核大小3x3
conv = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3,padding=1)

# 处理数据
output = conv(x)
print(output)

# 最大池化：取 2x2 区域的最大值
pool = nn.MaxPool2d(kernel_size=2)
result = pool(torch.relu(output))
print(result.shape)

# 平均池化：取 2x2 区域的平均值
pool = nn.AvgPool2d(kernel_size=2)
result = pool(torch.relu(output))
print(result.shape)

# 展平
output = output.view(output.size(0), -1)
print(output.shape)

# 全连接层
linear = nn.Linear(in_features=output.size(1), out_features=128)
result = torch.relu(linear(output))

linear = nn.Linear(128, out_features=10)
result = linear(result) 
print(result.shape)

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3,padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(32 * 16 * 16, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv(x)))
        x = x.view(-1, 32 * 16 * 16)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 测试
model = CNN()
x = torch.randn(10,1,32,32)
print(model(x).shape)

# 定义 RNN
rnn = nn.RNN(input_size=10, hidden_size=20, num_layers=1, batch_first=True)

# 输入
x = torch.randn(32, 5, 10)

# 前向计算
output, h_n = rnn(x)
print(output.shape)  
print(h_n.shape) 

# 定义 LSTM
lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=1, batch_first=True)

x = torch.randn(32, 5, 10)

# 前向计算
output, (h_n, c_n) = lstm(x)
print(output.shape)
print(h_n.shape)
print(c_n.shape)

import torch.nn as nn

# Transformer 编码器层
encoder_layer = nn.TransformerEncoderLayer(
    d_model=512,       # 特征维度
    nhead=8,           # 注意力头数
    dim_feedforward=2048, # 前馈网络隐藏层维度
    dropout=0.1,         # 丢弃概率
    batch_first=True,
)

# 堆叠 N 层
transformer = nn.TransformerEncoder(encoder_layer, num_layers=6)

# 输入：(seq_len, batch, d_model)
src = torch.rand(10, 32, 512)
output = transformer(src)
print(output.shape) 

# Decoder 层
decoder_layer = nn.TransformerDecoderLayer(
    d_model=512,
    nhead=8,
    dim_feedforward=2048,
    dropout=0.1,
    batch_first=True
)

# 堆叠 6 层
decoder = nn.TransformerDecoder(decoder_layer, num_layers=6)

# 输入
memory = torch.rand(32, 10, 512)   # Encoder 的输出（理解结果）
tgt = torch.rand(32, 8, 512)       # 目标序列（要生成的内容）

# 训练
output = decoder(tgt, memory)
print(output.shape)

# 使用（推理）
decoder.eval()
with torch.no_grad():
    output = decoder(tgt, memory)
    print(output.shape) 