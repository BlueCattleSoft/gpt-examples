import os
from openai import OpenAI

OPENAI_API_KEY="..."

client = OpenAI(api_key=OPENAI_API_KEY)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[{"role": "user", "content": "Which country is Paris located in?"}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
