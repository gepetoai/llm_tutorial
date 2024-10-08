# Import necessary libraries
from pydantic import BaseModel
import instructor
from dotenv import load_dotenv
from anthropic import Anthropic
from typing import Literal

# Load environment variables
load_dotenv()

# Define the system prompt
system_prompt = "Your job is to decide whether or not to escalate to a manager."

# Define k-shot examples
k_shot = '''
EXAMPLE 1:
User: My FOH isn't working.
Assistant: False, the customer is asking a support question that we can answer.

EXAMPLE 2:
User: I hate you.
Assistant: True, the customer is expressing negative emotions towards the staff.

EXAMPLE 3:
User: I'm a dealer.
Assistant: True, the customer is a dealer and needs to be escalated to a manager.
'''

# Append k-shot examples to the system prompt
system_prompt += k_shot

# Define user input
user_input = "My FOH isn't working."

# Define Pydantic model for the response
class ToEscalate(BaseModel):
    escalate: bool
    reason: str

# Initialize Anthropic client using instructor
client = instructor.from_anthropic(Anthropic())

# Make an API call to generate a response
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

# Print the response
print(resp)
