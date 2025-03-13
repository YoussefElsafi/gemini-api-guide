from google import genai
from google.genai import types
import requests
import pathlib
import PIL.Image
import os

# Image Files
image_path_1 = "Images/Example_Image.png"  # First image path
image_path_2 = "Images/Example_Image2.jpg" # Second image path
pil_image = PIL.Image.open(image_path_1) # Load the first image
b64_image = types.Part.from_bytes(
    data=pathlib.Path(image_path_2).read_bytes(), # Load the second image
    mime_type="image/jpg" # The image format
)

# Image URLs
image_url_1 = "https://goo.gle/instrument-img" # Image URL
downloaded_image = requests.get(image_url_1) # Download the Image

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Generate the response
response = client.models.generate_content(
    model="gemini-2.0-flash", # The model
    contents=[
        "What do these images have in common?", # The Message input to the AI
        pil_image, # Image path 1 loaded using Pillow python library
        b64_image, # The Base64 encoded image
        downloaded_image # The downloaded image for the Image URL
    ]
)

# Print the response
print(response.text)