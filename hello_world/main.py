from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role":"system", "content":"You are an expert in Maths and only and only ans maths related questions. If the query is not related to maths say sorry and don't answer the question"},
    {"role": "user", "content": "Hey, can you help me solve a + b whole square"}
  ]
)
print(response.choices[0].message.content)