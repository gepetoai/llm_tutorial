from pydantic import BaseModel
import instructor
from dotenv import load_dotenv
from anthropic import Anthropic
from openai import OpenAI
from typing import Literal

load_dotenv()

system_prompt = "Your job is to update a menu based on the user's request."
user_input = "Add pizza for $10. its a delicious pizza."

class MenuUpdate(BaseModel):
    name: str
    price: float
    description: str

client = instructor.from_anthropic(Anthropic())
#client = instructor.from_openai(OpenAI())

resp = client.chat.completions.create(
    model="claude-3-5-sonnet-20240620", #model = "gpt-4o"
    response_model=MenuUpdate,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ],
    temperature=0,
    max_tokens=100
)

print(resp)

