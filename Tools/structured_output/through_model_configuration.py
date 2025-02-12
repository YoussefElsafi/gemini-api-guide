from google import genai
from pydantic import BaseModel, TypeAdapter
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

class Recipe(BaseModel):
    """
    A simple recipe class with two fields: recipe_name and ingredients.
    """
    recipe_name: str
    ingredients: list[str]

# Generate the response
response = client.models.generate_content(
    model='gemini-2.0-flash', # The AI Model
    contents='List a few popular cookie recipes.', # The input prompt to the AI
    config={ # Model configuration
        'response_mime_type': 'application/json', # The response type
        'response_schema': list[Recipe], # The response schema
    },
)

# Print the response
print(response.text) # Note: You can use the response as a JSON string.

# Use instantiated objects.
my_recipes: list[Recipe] = response.parsed