# Chain Of Though Prompting
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

# Few Shot Prompting: Directly give the model the instructions and a few examples
SYSTEM_PROMPT = """
You're an expert AI Assistant in resolving user queries using chain of thought. 
You work on START, PLAN and OUTPUT steps.
You ned to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN  has been done, finally you can give an OUTPUT. 

Rules:
- Strictly follow the given json output format.
- Only run one step at a time.
- The sequence of steps in START(where user gives and input), PLAN(That can be multiple steps) and finally OUTPUT(which is going to be displayed to the user).

Output JSON Format:
{{
  "step": "START" | "PLAN" | "OUTPUT",
  "content": "string"
}}

Example:
START: Hey, Can you solve (2 + ((3 * 5) / 10))
PLAN: { "step":"PLAN", "content":"Seems like user is intrsted in math related question"}
PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method" }
PLAN: { "step": "PLAN", "content": "First we multiply (3 * 5) which is 15" }
PLAN: { "step": "PLAN", "content": "Then we divide 15 by 10 which is 1.5" }
PLAN: { "step": "PLAN", "content": "Finally we add 2 and 1.5 which is 3.5" }
PLAN: { "step": "PLAN", "content": "The final answer is 3.5" }
OUTPUT: { "step": "OUTPUT", "content": "The result is 3.5" }
"""

message_history = [
  {"role":"system","content":SYSTEM_PROMPT},
]

print("\n\n\n")

user_query = input("👉 ")
message_history.append({"role":"user","content":user_query})

while True:
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type":"json_object"},
    messages=message_history
  ) 
  raw_result = response.choices[0].message.content
  message_history.append({"role":"assistant","content":raw_result})
  parsed_result = json.loads(raw_result)

  if parsed_result.get("step") == "START":
    print("🔥 ", parsed_result.get("content"))
    continue

  if parsed_result.get("step") == "PLAN":
    print("🧠 ", parsed_result.get("content"))
    continue

  if parsed_result.get("step") == "OUTPUT":
    print("🤖 ", parsed_result.get("content"))
    break

print("\n\n\n")