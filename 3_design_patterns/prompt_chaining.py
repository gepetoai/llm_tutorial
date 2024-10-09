# Import necessary libraries
from pydantic import BaseModel
import instructor
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# Define Pydantic models for data validation
class Country(BaseModel):
    name: str

class DishName(BaseModel):
    dish_name: str
    vegetarian_only: bool

# Function to get a dish name based on a country
def get_dish_name(country: Country) -> DishName:
    # Define the system prompt with instructions
    system_prompt = "You brainstorm the name of one dish based on the country. Only give one dish. Below are examples\n"
    # Add k-shot examples to the system prompt
    k_shot = '''
        Country: Japan
        dish_name: Sushi
        vegetarian_only: False

        Country: Italy
        dish_name: Pizza
        vegetarian_only: False

        Country: Mexico
        dish_name: Tacos
        vegetarian_only: False

        Country: India
        dish_name: palak_paneer
        vegetarian_only: True
    '''

    system_prompt += k_shot

    # Initialize the Anthropic client
    client = instructor.from_anthropic(Anthropic())

    # Make an API call to generate a dish name
    resp = client.chat.completions.create(
        model="claude-3-5-sonnet-20240620", 
        response_model=DishName,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": country.name}
        ],
        temperature=0,
        max_tokens=100
    )

    return resp

# Example usage of get_dish_name function
resp = get_dish_name(Country(name="Pakistan"))

# Define Pydantic model for recipe
class Recipe(BaseModel):
    ingredients: list[str]
    instructions: list[str]
    substitution_notes: str

# Function to create a recipe based on a dish name
def create_recipe(dish: DishName) -> Recipe:
    # Define the system prompt with instructions for recipe creation
    system_prompt = '''
    You are a culinary expert. 
    Create a recipe for the given dish, including ingredients, instructions, and vegetarian substitution notes if applicable. 
    If it's a vegetarian dish, give notes on how to make it non-vegetarian. 
    If it's non-vegetarian, give notes on how to make it vegetarian.

    Keep your ingredients and insturctions concise and to the point
    '''
    
    # Initialize the Anthropic client
    client = instructor.from_anthropic(Anthropic())

    # Make an API call to generate a recipe
    resp = client.chat.completions.create(
        model="claude-3-5-sonnet-20240620",
        response_model=Recipe,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Create a recipe for {dish.dish_name}. Is it vegetarian only: {dish.vegetarian_only}"}
        ],
        temperature=0,
        max_tokens=1000
    )

    return resp

# Example usage of the entire prompt chain
dish_name = get_dish_name(Country(name="France"))
recipe = create_recipe(dish_name)

# Print the generated recipe
print(f"Recipe for {dish_name.dish_name}:")
print(f"Ingredients:\n{recipe.ingredients}\n")
print(f"Instructions:\n{recipe.instructions}\n")
print(f"Vegetarian substitution notes:\n{recipe.substitution_notes}\n")
