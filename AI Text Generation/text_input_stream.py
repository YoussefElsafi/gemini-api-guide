from google import genai
import os

# Your Message to the AI
prompt = "Hello, how are you?"

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)


response = client.models.generate_content_stream(model="gemini-2.0-flash", contents=prompt) # Generate the response
for chunk in response: # Collect the response
    print(chunk.text, end="") # Print the response in chunks