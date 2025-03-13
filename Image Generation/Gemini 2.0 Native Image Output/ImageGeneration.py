from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Text prompt to the model
contents = ('Hi, can you create a 3d rendered image of a pig '
            'with wings and a top hat flying over a happy ' 
            'futuristic scifi city with lots of greenery?')

# Generate the image
response = client.models.generate_content(
    model="models/gemini-2.0-flash-exp", # The model that supports image generation
    contents=contents, # The text prompt for the model
    config=types.GenerateContentConfig( # The configuration for the model
      response_modalities=[ # The response modalities for the model
        'Text', # The text response
        'Image' # The image response
        ],
        temperature = 1 # 1 is recommended for image generation
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
    image.show(f"[ generated_images/image_{image_number}.png ] - Generated Image")
    print()