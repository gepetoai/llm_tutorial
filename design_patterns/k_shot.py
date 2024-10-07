from pydantic import BaseModel
import instructor
from dotenv import load_dotenv
from anthropic import Anthropic
from typing import Literal

load_dotenv()

system_prompt = "Your job is to decide whether or not to escalate to a manager."
user_input = "My FOH isn't working."

class ToEscalate(BaseModel):
    escalate: bool
    reason: str

client = instructor.from_anthropic(Anthropic())

resp = client.chat.completions.create(
    model="claude-3-5-sonnet-20240620", 
    response_model=ToEscalate,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ],
    temperature=0,
    max_tokens=100
)

print(resp)

