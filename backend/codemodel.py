from openai import OpenAI
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("DEEPSEEKAPIKEY")


def getResponse(userInput):
    client = OpenAI(api_key=openai.api_key, base_url="https://api.deepseek.com/v1")

    response = client.chat.completions.create(
        model="deepseek-coder",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": userInput},
        ]
    )
    return response.choices[0].message.content
