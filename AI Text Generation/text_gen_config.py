from google import genai
from google.genai import types
import os

# Your Message to the AI
prompt = "Explain how AI works"

# API Key
API_KEY = os.environ["API_KEY"] # Get your API Key at https://aistudio.google.com
client = genai.Client(api_key=API_KEY)

# Generate the response
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[prompt], # The input to the AI
    config=types.GenerateContentConfig(
        max_output_tokens=500, # The maximum number of tokens to output
        temperature=0.1 # The creativity allowed in the response, Max is 2
    )
)

# Print the response
print(response.text)