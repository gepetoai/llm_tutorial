# Import necessary libraries
from pydantic import BaseModel
import instructor
from dotenv import load_dotenv
from anthropic import Anthropic
from typing import List

# Load environment variables
load_dotenv()

# Define the system prompt for the AI
system_prompt = "Your job is to answer the user's question."
# Define the user input
user_input = "Why is the sky blue?"

class ThoughtfulAnswer(BaseModel):
    candidate_answers: List[str]
    final_answer: str

# Initialize the Anthropic client using instructor
client = instructor.from_anthropic(Anthropic())

# Make an API call to generate a menu update
resp = client.chat.completions.create(
    model="claude-3-5-sonnet-20240620", 
    response_model=ThoughtfulAnswer,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ],
    temperature=0,  
    max_tokens=1000  # Limit the response length
)

# Print the generated menu update
print(resp.candidate_answers)
print(resp.final_answer)
