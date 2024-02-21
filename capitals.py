import os
import sys
from openai import OpenAI

try:
    with open("APIKEY", 'r') as file:
        OPENAI_API_KEY = file.read()
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    sys.exit(0)
except Exception as e:
    print("An error occurred:", e)
    sys.exit(0)

client = OpenAI(api_key=OPENAI_API_KEY)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[{"role": "system", "content": "The user gives you countries and your task is to answer with the capital city"}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
