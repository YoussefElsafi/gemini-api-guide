from google import genai
import os

# Your Message to the AI
prompt = "Hello, how are you?"

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt) # Generate the response
print(response.text, end="") # Print the response