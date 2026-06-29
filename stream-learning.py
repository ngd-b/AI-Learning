from openai import OpenAI
from dotenv import load_dotenv
import os
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from pydantic import BaseModel
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# 初始化创建 OpenAI 对象,从.env 中获取 API KEY
load_dotenv(override=True)

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")

client = OpenAI(api_key=api_key, base_url=base_url)


# async def main():
#     async for _ in call_model([{"role": "user", "content": "Hi"}]):
#         pass
def main():
    call_model([{"role": "user", "content": "你是谁，详细介绍？"}])


# async def call_model(messages):
def call_model(messages):
    # 加系统提示词，并且添加 JSON 提示
    system_prompt = """
    All result must be a json object
    {
        "answer": "The answer to the question",
        "question": "The question asked"
    }
    """

    messages.insert(0, {"role": "system", "content": system_prompt})

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=messages,
        stream=True,
        reasoning_effort="high",
        response_format={"type": "json_object"},
        extra_body={"thinking": {"type": "enabled"}},
    )

    result = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            # 打字机效果
            print(content, end="", flush=True)
            result += content
            # yield {"data": content}

    return result


class ChatRequest(BaseModel):
    messages: list[dict]


async def stream_api(messages):
    # 加系统提示词，并且添加 JSON 提示
    system_prompt = """
    All result must be a json object
    {
        "answer": "The answer to the question",
        "question": "The question asked"
    }
    """

    messages.insert(0, {"role": "system", "content": system_prompt})

    async with httpx.AsyncClient() as client:
        async with client.stream(
            "POST",
            "https://api.deepseek.com/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "deepseek-v4-pro",
                "messages": messages,
                "stream": True,
                "thinking": {"type": "enabled"},
                "reasoning_effort": "high",
            },
        ) as response:
            async for line in response.aiter_lines():
                if line.startswith("data: "):
                    chunk = line[6:]  # 去掉 "data: " 前缀
                    if chunk != "[DONE]":
                        yield chunk


@app.post("/chat")
async def chat(req: ChatRequest):
    # return EventSourceResponse(call_model(req.messages))
    return EventSourceResponse(stream_api(req.messages))


if __name__ == "__main__":
    # asyncio.run(main())
    main()
