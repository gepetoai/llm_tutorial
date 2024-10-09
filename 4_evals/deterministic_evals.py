# Import necessary libraries
from typing import Literal
from pydantic import BaseModel
import instructor
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Define a Pydantic model
class ProduceType(BaseModel):
    type: Literal["fruit", "vegetable", "neither"]

def determine_produce_type(produce_name: str) -> ProduceType:
    # Define the system prompt for the AI
    system_prompt = "Your job is to determine if it's a fruit, vegetable, or neither."

    # Initialize the Anthropic client using instructor
    client = instructor.from_openai(OpenAI())

    # Make an API call to generate a menu update
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        response_model=ProduceType,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": produce_name}
        ],
        temperature=0,  
        max_tokens=100  # Limit the response length
    )

    return resp


produces = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("lettuce", "vegetable"),
    ("potato", "vegetable"),
    ("tomato", "fruit"),
    ("onion", "vegetable"),
    ("garlic", "vegetable"),
    ("ginger", "vegetable"),
    ("salt", "neither"),
    ("fish", "neither"),
    ("olive oil", "neither"),
    ("vinegar", "neither"),
    ("sugar", "neither"),
]

correct_count = 0
total_count = len(produces)

# Evaluate the model
for produce, expected_type in produces:
    result = determine_produce_type(produce).type
    correct = result == expected_type
    # increment correct count
    correct_count += int(correct)
    if not correct:
        print(f"Produce: {produce}, Expected: {expected_type}, Result: {result}")

accuracy = correct_count / total_count
print(f"\nEvaluation Results:")
print(f"Total items: {total_count}")
print(f"Correct predictions: {correct_count}")
print(f"Accuracy: {accuracy:.2%}")

