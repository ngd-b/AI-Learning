# AI-Learning

前端转 AI 工程师学习项目 — 以代码实践驱动，逐阶段掌握 AI 工程核心能力。

---

## 学习路线 & 进度

### 第一阶段：Python 核心能力 ✅

> 目标：能用 Python 独立写脚本、调 API、处理数据

- [x] 环境搭建（Python / pyenv / 虚拟环境）
- [x] 基础语法速通
- [x] 文件 I/O 与数据处理
- [x] 常用标准库：`json`, `os`, `sys`, `argparse`, `tempfile`
- [x] 包管理：`pip` + `venv`
- [x] Jupyter Notebook 基础

**实战项目：**
- [translate-cli.py](translate-cli.py) — AI 翻译 CLI 工具，读取 JSON → 调用 OpenAI 兼容 API 翻译 → 写回文件
- [main-2026-5-25.py](main-2026-5-25.py) / [main-2026-5-26.py](main-2026-5-26.py) — 早期 Python 练习

---

### 第二阶段：数据处理三板斧 ✅

> 目标：熟练操作结构化 / 非结构化数据

- [x] **NumPy** — 数组创建、运算、切片、变形
- [x] **Pandas** — Series / DataFrame、数据筛选、分组聚合、缺失值处理、CSV/Excel 读写
- [x] **Matplotlib** — 折线图、柱状图、饼图、散点图、热力图、多子图、高清导出

**学习笔记：**
- [numpy-learning.py](numpy-learning.py)
- [pandas-learning.py](pandas-learning.py)
- [matplotlib-learning.py](matplotlib-learning.py)

**实战项目：**
- [data-analysis.py](data-analysis.py) — 泰坦尼克号生存数据分析：数据清洗 → 可视化 → 相关性分析 → 结论输出

---

### 第三阶段：机器学习基础 🔲

> 目标：理解 ML 核心概念，能跑通经典模型

- [ ] **Scikit-learn** — 分类、回归、聚类、模型评估
- [ ] 核心概念：训练集/验证集/测试集划分、特征工程、过拟合与交叉验证
- [ ] 经典算法：线性回归、逻辑回归、决策树、随机森林、K-Means
- [ ] 常用指标：准确率、精确率、召回率、F1、AUC

**计划实战：** Kaggle Titanic 竞赛进阶（从人工分析过渡到模型预测）

---

### 第四阶段：深度学习入门 🔲

> 目标：理解神经网络原理，能用 PyTorch 搭建简单模型

- [ ] **PyTorch** 基础：Tensor、Autograd、nn.Module、DataLoader
- [ ] 前馈神经网络（全连接层、激活函数、反向传播）
- [ ] CNN — 图像分类入门
- [ ] RNN / LSTM — 序列数据处理
- [ ] **Transformer 架构**：Self-Attention、位置编码、Encoder-Decoder
- [ ] **Hugging Face 生态**：Hub、Datasets、Transformers、Spaces

**计划实战：** MNIST 手写数字识别 / 文本情感分类

---

### 第五阶段：大语言模型 & 应用开发 🔲

> 目标：掌握 LLM 生态，能独立开发 AI 应用

#### 5.1 LLM 基础
- [ ] GPT 原理（预训练 → 微调 → RLHF）
- [ ] Prompt Engineering（Few-shot / Chain-of-Thought / ReAct）
- [ ] Structured Output / JSON Mode
- [ ] Streaming 流式响应（SSE）
- [ ] 模型选型与对比

#### 5.2 RAG（检索增强生成）
- [ ] LangChain / LlamaIndex 框架
- [ ] 向量数据库：Chroma / FAISS / Milvus
- [ ] Embedding 模型
- [ ] RAG 完整流程：文档加载 → 分块 → 向量化 → 检索 → 生成

#### 5.3 Agent 开发
- [ ] Function Calling / Tool Use
- [ ] ReAct 模式
- [ ] 多 Agent 协作
- [ ] 记忆系统

#### 5.4 模型评估 & 可观测性
- [ ] LangSmith / LangFuse
- [ ] Prompt 版本管理 & A/B 测试

**计划实战：** 个人知识库问答系统

---

### 第六阶段：模型微调 & 部署 🔲

> 目标：能针对业务场景微调模型，并部署上线

- [ ] LoRA / QLoRA 微调
- [ ] 数据集准备与格式转换
- [ ] FastAPI 模型服务化
- [ ] 推理优化：vLLM / Ollama
- [ ] Docker 容器化部署
- [ ] 成本控制：Token 计量、Prompt Caching、模型分层策略

---

### 第七阶段：进阶方向 🔲

| 方向 | 技术栈 |
| --- | --- |
| AI 全栈开发 | Next.js + Vercel AI SDK + LangChain |
| 多模态 AI | CLIP, Stable Diffusion, Whisper |
| MLOps | MLflow, W&B, K8s |
| AI Agent 架构 | LangGraph, CrewAI, AutoGen |

---

## 推荐资源

### 课程
- [fast.ai Practical Deep Learning](https://course.fast.ai/)
- [DeepLearning.AI 短课程](https://www.deeplearning.ai/courses/)
- [李宏毅机器学习](https://speech.ee.ntu.edu.tw/~hylee/ml/2023-spring.php)

### 文档
- [OpenAI Cookbook](https://cookbook.openai.com/)
- [LangChain 官方文档](https://python.langchain.com/docs/)
- [Hugging Face Course](https://huggingface.co/learn/nlp-course)

---

## 环境

- Python 3.12+
- 已用依赖：`numpy`、`pandas`、`matplotlib`、`openai`、`python-dotenv`

```bash
python -m venv .venv && source .venv/bin/activate
pip install numpy pandas matplotlib openai python-dotenv
```
