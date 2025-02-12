from google import genai
from google.genai import types
import os
import requests

# Your message to the AI
prompt = "What is this image?"

# Load Image URL
image_URL = "https://goo.gle/instrument-img"  # Image URL
image = requests.get(image_URL)  # Download the image

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Generate the response
response = client.models.generate_content(
    model="gemini-2.0-flash",  # The model
    contents=[
        prompt,  # The message input to the AI
        types.Part.from_bytes(
            data=image.content,  # The image data
            mime_type="image/jpeg"  # The image format
        )
    ]
)

# Print the response
print(response.text)