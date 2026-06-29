from openai import OpenAI
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from string import Template
import tiktoken

# 初始化创建 OpenAI 对象,从.env 中获取 API KEY
load_dotenv(override=True)

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")

client = OpenAI(api_key=api_key, base_url=base_url)

# 提示词模板
prompt_template = Template("""
你是一个 $role，擅长 $skills。

任务：$task

输入：
$input

输出格式要求：
$output_format
""")
def main():
    
    prompt = "Hi"
    print(call_model([{"role": "user", "content": prompt}]))

    # 测试temperature
    # prompt="你很"
    # for temp in [0, 1,2]:
    #     output = call_model([{"role": "user", "content": prompt}])
    #     print(f"Temperature: {temp}")
    #     print(output)
        
    # 提示词
    prompt = f"""
    User: "英文 → 中文：
    hello → 你好
    goodbye → 再见
    apple → 苹果
    cat → ？"
    """
    print(call_model([{"role": "user", "content": prompt}]))
    
    # 不同场景传入不同参数
    test_code = f"""
    def add(a, b):
        return a + b
    """
    code_review_prompt = prompt_template.substitute(
        role="Python 代码审查专家",
        skills="性能优化、安全审计、代码规范",
        task="审查以下代码，输出问题列表和改进建议",
        input=test_code,
        output_format="JSON，字段：severity, line, issue, suggestion",
    )
    print(call_model([{"role": "user", "content": code_review_prompt}]))

    # 用通用编码器（大多数模型兼容此格式）
    enc = tiktoken.get_encoding("cl100k_base")

    text = "你好世界"
    tokens = enc.encode(text)
    print(len(tokens)) 
class Result(BaseModel):
    answer: str
    question: str      
# 调用大模型
def call_model(messages):
    # 加系统提示词，并且添加 JSON 提示
    # system_prompt="All result must be a json object"
    # 提示词定义结构化输出字段
    system_prompt = """
    All result must be a json object
    {
        "answer": "The answer to the question",
        "question": "The question asked"
    }
    """
    
    messages.insert(0, {"role": "system", "content": system_prompt})

    response = client.chat.completions.create(
    # response = client.chat.completions.parse(
        model="deepseek-v4-pro",
        messages=messages,
        stream=False,
        reasoning_effort="high",
        # response_format=Result,
        response_format={"type": "json_object"},
        extra_body={"thinking": {"type": "enabled"}}
    )
    
    return response.choices[0].message.content
    # return response.choices[0].message.parsed

if __name__ == "__main__":
    main()
