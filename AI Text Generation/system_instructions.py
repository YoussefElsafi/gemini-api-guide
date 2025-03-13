from google import genai
from google.genai import types
import os

# Your Message to the AI
prompt = "Hello! What's your name?"

# Your system instructions to the AI
sys_instruct="You are a cat. Your name is Neko."

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Generate the response
response = client.models.generate_content(
    model="gemini-2.0-flash", # The model
    config=types.GenerateContentConfig(
        system_instruction=sys_instruct # The system instruction input to the AI
    ),
    contents=[prompt] # The input to the AI
)

print(response.text) # Print the response