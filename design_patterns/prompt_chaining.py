from pydantic import BaseModel
import instructor
from dotenv import load_dotenv
from anthropic import Anthropic
from typing import Literal

load_dotenv()

class Country(BaseModel):
    name: str

class DishName(BaseModel):
    dish_name: str
    vegetarian_only: bool

def get_dish_name(country: Country) -> DishName:
    system_prompt = "You brainstorm the name of one dish based on the country. Only give one dish. Below are examples\n"
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

    client = instructor.from_anthropic(Anthropic())

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

resp = get_dish_name(Country(name="Pakistan"))


class Recipe(BaseModel):
    ingredients: list[str]
    instructions: list[str]
    substitution_notes: str

def create_recipe(dish: DishName) -> Recipe:
    system_prompt = '''
    You are a culinary expert. 
    Create a recipe for the given dish, including ingredients, instructions, and vegetarian substitution notes if applicable. 
    If it's a vegetarian dish, give notes on how to make it non-vegetarian. 
    If it's non-vegetarian, give notes on how to make it vegetarian.

    Keep your ingredients and insturctions concise and to the point
    '''
    
    client = instructor.from_anthropic(Anthropic())

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

# Example usage
dish_name = get_dish_name(Country(name="France"))
recipe = create_recipe(dish_name)
print(f"Recipe for {dish_name.dish_name}:")
print(f"Ingredients:\n{recipe.ingredients}\n")
print(f"Instructions:\n{recipe.instructions}\n")
print(f"Vegetarian substitution notes:\n{recipe.substitution_notes}\n")
