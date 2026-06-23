import torch
from torchvision import datasets,transforms
import torch.nn as nn
from torch.utils.data import DataLoader
import torch.optim as optim
from PIL import Image,ImageOps

# 预处理：转成 Tensor + 标准化
transform = transforms.Compose([
    transforms.ToTensor(),                     # PIL 图片 → Tensor，同时把 0-255 缩到 0-1
    transforms.Normalize((0.1307,), (0.3081,)) # 标准化，让数据分布更稳定
])

# 下载 MNIST（第一次会下载，之后用缓存）
train_dataset = datasets.MNIST("./data", train=True, download=True, transform=transform)
test_dataset = datasets.MNIST("./data", train=False, transform=transform)

print(f"训练集大小：{len(train_dataset)} 张")
print(f"测试集大小：{len(test_dataset)} 张")
print(f"一张图的 shape：{train_dataset[0][0].shape}")  
print(f"对应标签：{train_dataset[0][1]}") 

# DataLoader 把数据切成小批（batch），每次喂 64 张图给模型
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=1000)  

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        # 卷积层：提取图像特征
        self.conv1 = nn.Conv2d(1, 32, 3, 1,padding=1)    # 输入 1 通道（灰度），输出 32 通道
        self.conv2 = nn.Conv2d(32, 64, 3, 1,padding=1)   # 32 → 64 通道
        # 全连接层：分类
        self.fc1 = nn.Linear(12544, 128)          # 展平后 64×14×14 = 12544
        self.fc2 = nn.Linear(128, 10)            # 输出 10 类（数字 0-9）

    def forward(self, x):
        x = torch.relu(self.conv1(x))           # conv1 + ReLU
        x = torch.relu(self.conv2(x))           # conv2 + ReLU
        x = torch.max_pool2d(x, 2)              # 2×2 池化，尺寸减半
        x = torch.flatten(x, 1)                 # 展平成一维向量
        x = torch.relu(self.fc1(x))             # 全连接 + ReLU
        x = self.fc2(x)                         # 输出 10 个分数（不加激活，Loss 内置 Softmax）
        return x

model = CNN()

# 损失函数
criterion = nn.CrossEntropyLoss()                # 多分类损失函数
optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adam 优化器

for epoch in range(5):
    model.train()                                # 切换到训练模式
    total_loss = 0
    for batch_X, batch_y in train_loader:
        optimizer.zero_grad()                    # 清空上一轮梯度
        output = model(batch_X)                  # 前向传播
        loss = criterion(output, batch_y)        # 算损失
        loss.backward()                          # 反向传播，算梯度
        optimizer.step()                         # 更新参数

        total_loss += loss.item() * batch_X.size(0)   # 乘以这个 batch 的样本数
    print(f"Epoch {epoch+1}, Avg Loss: {total_loss / len(train_dataset):.4f}")
    
model.eval()                                     # 切换到评估模式
correct = 0
total = 0
with torch.no_grad():                            # 不计算梯度，省显存、加速
    for batch_X, batch_y in test_loader:
        output = model(batch_X)
        pred = output.argmax(dim=1)              # 取分数最高的那个类别
        correct += (pred == batch_y).sum().item()
        total += batch_y.size(0)

print(f"测试准确率：{correct / total:.4f}") 

torch.save(model.state_dict(), "mnist_cnn.pth")

# 加载你的图片，转灰度、缩放到 28×28
img = Image.open("test-eight.jpg").convert("L").resize((28, 28))
img = ImageOps.invert(img)   # 黑白反转，变黑底白字

# 转成和训练数据一样的格式
img_tensor = transforms.ToTensor()(img)      # [1, 28, 28]，0-1
img_tensor = transforms.Normalize((0.1307,), (0.3081,))(img_tensor)  # 标准化

# 预测
with torch.no_grad():
    pred = model(img_tensor.unsqueeze(0)).argmax(dim=1).item()
print(f"识别结果: {pred}")