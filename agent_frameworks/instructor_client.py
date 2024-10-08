# Import necessary libraries
from pydantic import BaseModel
import instructor
from dotenv import load_dotenv
from anthropic import Anthropic
from openai import OpenAI
from typing import Literal

# Load environment variables
load_dotenv()

# Define the system prompt for the AI
system_prompt = "Your job is to update a menu based on the user's request."
# Define the user input
user_input = "Add pizza for $10. its a delicious pizza."

# Define a Pydantic model for menu updates
class MenuUpdate(BaseModel):
    name: str
    price: float
    description: str

# Initialize the Anthropic client using instructor
client = instructor.from_anthropic(Anthropic())
# Alternatively, use OpenAI client (commented out)
#client = instructor.from_openai(OpenAI())

# Make an API call to generate a menu update
resp = client.chat.completions.create(
    model="claude-3-5-sonnet-20240620", # For OpenAI, use: model = "gpt-4o"
    response_model=MenuUpdate,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ],
    temperature=0,  
    max_tokens=100  # Limit the response length
)

# Print the generated menu update
print(resp)
