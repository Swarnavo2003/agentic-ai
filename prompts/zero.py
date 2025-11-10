from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Zero Shot Prompting: Directly give the model the instructions
SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not answer anything else. Your name is Alexa. I f user asks you a question that is not related to coding, say sorry and don't answer the question"

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role":"system", "content":SYSTEM_PROMPT},
    {"role": "user", "content": "Hey, can write a python code to translate a sentence from english to hindi"}
  ]
)
print(response.choices[0].message.content)