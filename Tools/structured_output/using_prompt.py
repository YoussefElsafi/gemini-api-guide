from google import genai
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Prompt the AI to list a few popular cookie recipes in JSON format.
prompt = """List a few popular cookie recipes in JSON format.

Use this JSON schema:

Recipe = {'recipe_name': str, 'ingredients': list[str]}
Return: list[Recipe]"""

# Generate the response
response = client.models.generate_content(
    model='gemini-2.0-flash', # The AI Model
    contents=prompt, # The input prompt to the AI
)

# Print the response
print(response.text) # Note: You can use the response as a JSON string.