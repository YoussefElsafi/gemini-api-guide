from google import genai
import os
import PIL.Image

# Your Message to the AI
prompt = "What is this image?"

image = PIL.Image.open('Images/Example_Image.png') # Path to the image

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Generate the response
response = client.models.generate_content(
    model="gemini-2.0-flash", # The model
    contents=[
        prompt, # The Message input to the AI
        image # The image input to the AI
    ]
)

print(response.text)