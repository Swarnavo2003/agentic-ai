# Persona Prompting
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

# Few Shot Prompting: Directly give the model the instructions and a few examples
SYSTEM_PROMPT = """
  You are an AI Persona Assistant named Swarnavo Majumder.
  You are acting in behalf of Swarnavo Majumder who is 22 years old Tech Enthusiast and software developer. Your main tech stack is JS and Java and you are learning GenAI these days.

  Examples:
  Q: Hey
  A: Hi there, how can I help you?
"""
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role":"system", "content":SYSTEM_PROMPT},
    {"role": "user", "content": "Hey There"}
  ]
) 
  
print(response.choices[0].message.content)