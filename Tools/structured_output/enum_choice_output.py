from google import genai
import enum
from pydantic import BaseModel
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Enum Class for the Grade
class Grade(enum.Enum):
    A_PLUS = "a+"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    F = "f"

# Recipe Class
class Recipe(BaseModel):
  recipe_name: str
  rating: Grade

# Generate the response
response = client.models.generate_content(
    model='gemini-2.0-flash', # The AI Model
    contents='List 10 home-baked cookies and give them grades based on tastiness.', # The input prompt to the AI
    config={ # Model configuration
        'response_mime_type': 'application/json', # The response type
        'response_schema': list[Recipe], # The response schema
    },
)

# Print the response
print(response.text)
# Example Answer: [{"rating": "a+", "recipe_name": "Classic Chocolate Chip Cookies"}, ...]