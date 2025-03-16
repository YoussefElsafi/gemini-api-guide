from flask import cli
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Text prompt to the model
contents = ('Add some chocolate drizzle to the croissants.')


img_path = r"images\croissant.jpeg" # The path to the image
image = client.files.upload(file=img_path) # Upload the image to gemini


# Generate the image
response = client.models.generate_content(
    model="models/gemini-2.0-flash-exp-image-generation", # The model that supports image generation
    contents=[
      image, # The image input to the AI for editing it
      contents # The text prompt for the model
    ],
    config=types.GenerateContentConfig( # The configuration for the model
      response_modalities=[ # The response modalities for the model
        'Text', # The text response
        'Image' # The image response
        ],
        temperature = 0 # 0 is recommended for image editing
    )
)

# Save & Display the generated image & text
image_number = len(os.listdir("generated_images/")) + 1 # Counts how many images are there
for part in response.candidates[0].content.parts: # Loop through the parts of the response
  if part.text is not None: # If the part is text
    print(part.text)
  elif part.inline_data is not None: # If the part is an image
    # Save the image
    image = Image.open(BytesIO(part.inline_data.data))
    image.save(f"generated_images/image_{image_number}.png")
    print(f"[ generated_images/image_{image_number}.png ] - Generated Image")
    print()
