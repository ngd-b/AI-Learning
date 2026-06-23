from transformers import pipeline
from huggingface_hub import snapshot_download
from datasets import load_dataset

# 情感分析
classifier = pipeline("sentiment-analysis")
print(classifier("I hate this!"))

# 文本生成
generator = pipeline("text-generation", model="gpt2")
print(generator("I previously", max_length=50)[0]["generated_text"])

# 下载整个模型文件夹
snapshot_download("google/bert_uncased_L-2_H-128_A-2", local_dir="./models/bert")

# 加载 Hugging Face 上的公开数据集
dataset = load_dataset("stanfordnlp/imdb")           # IMDB 电影评论
print(dataset)
print(dataset["train"][0])

# 加载本地数据
dataset = load_dataset("csv", data_files="train.csv")
print(dataset)
