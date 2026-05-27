"""
需求：写一个 CLI 工具，读取 JSON 文件 → 调 OpenAI API 做文本翻译 → 写回文件。
"""

import json
import os
import sys
import tempfile
from openai import OpenAI
from dotenv import load_dotenv


def main():
    # 先接收cli参数，参数不存在，直接中断执行
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <json_file>")
        sys.exit(1)

    # 获取到json 文件路径，读取文件
    json_file = sys.argv[1]

    # 如果文件不存在，直接中断执行
    if not os.path.exists(json_file):
        print(f"File 【{json_file}】 does not exist.")
        sys.exit(1)

    # 初始化创建 OpenAI 对象,从.env 中获取 API KEY
    load_dotenv()

    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    if not api_key or not base_url:
        print("Missing API_KEY or BASE_URL in .env file.")
        sys.exit(1)

    client = OpenAI(api_key=api_key, base_url=base_url)

    try:
        # 读取文件
        with open(json_file, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        sys.exit(1)

    # 调用 AI 翻译内容
    translated_text = translate(client, data)

    # 写入追加到文件
    result = {"original": data, "translated": translated_text}
    safe_write(json_file, result)


# 安全写入文件,先写入临时文件，在替换原文件
def safe_write(file_path, content):
    dirname = os.path.dirname(file_path) or "."

    with tempfile.NamedTemporaryFile(
        mode="w", dir=dirname, delete=False, suffix=".tmp", encoding="utf-8"
    ) as tmp:
        json.dump(content, tmp, ensure_ascii=False, indent=4)

    os.replace(tmp.name, file_path)


# 定义调用AI方法，返回结果
def translate(client, text):
    """
    调用AI方法
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Return the text into English.",
                },
                {"role": "user", "content": text},
            ],
            stream=False,
            reasoning_effort="high",
            extra_body={"thinking": {"type": "enabled"}},
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"API call Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
