from google import genai
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

print("Listing available Gemini models:")
# List existing tuned models
for model_info in client.models.list():
    print(f"  - {model_info.name}")

# Print a message if no models are found
if len(client.models.list()) == 0:
    print("No tuned models found.")