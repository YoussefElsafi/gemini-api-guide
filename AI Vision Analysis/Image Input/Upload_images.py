# Upload images to gemini is used for files or images larger than 20MB

from google import genai
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Image
img_path = "Images/Example_Image.png" # The path to the image
file_ref = client.files.upload(file=img_path) # Upload the image to gemini
print(f'{file_ref=}') # Print the file reference

print("\n") # Print a new line

response = client.models.generate_content(
    model="gemini-2.0-flash", # The model
    contents=[
        "What color is that cat?", # The message input to the AI
        file_ref # The image input to the AI
    ]
)

# Print the response
print(response.text)