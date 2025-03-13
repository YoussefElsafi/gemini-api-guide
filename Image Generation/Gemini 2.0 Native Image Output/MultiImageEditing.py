from flask import cli
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

chat_session = client.chats.create(
  model="models/gemini-2.0-flash-exp", # The model that supports image generation
  config=types.GenerateContentConfig( # The configuration for the model
    response_modalities=[ # The response modalities for the model
      'Text', # The text response
      'Image' # The image response
      ],
    temperature = 0 # 0 is recommended for image editing
    )
) # Create a chat session

# Image
img_path = r"images\car.jpg" # The path to the image
image = client.files.upload(file=img_path) # Upload the image to gemini

# First inputs to the AI
Prompt1 = ('Turn this car into a convertible.') # Text prompt to the model


# Generate the image
response1 = chat_session.send_message(
  [
      image, # The image input to the AI for editing it
      Prompt1 # The text prompt for the model
  ]
)

# Save & Display the generated image & text
image_number = len(os.listdir("generated_images/")) + 1 # Counts how many images are there
for part in response1.candidates[0].content.parts: # Loop through the parts of the response
  if part.text is not None: # If the part is text
    print(part.text)
  elif part.inline_data is not None: # If the part is an image
    # Save the image
    image = Image.open(BytesIO(part.inline_data.data))
    image.save(f"generated_images/image_{image_number}.png")
    print(f"[ generated_images/image_{image_number}.png ] - Generated Image")
    print()

# Second inputs to the AI
Prompt2 = ('Imagine the car full of beach stuff. And change the color to something that feels like summer. Explain as you go.') # Text prompt to the model

# Generate the image
response2 = chat_session.send_message(Prompt2) # The text prompt for the model & No need to re-upload the image

# Save & Display the generated image & text
for part in response2.candidates[0].content.parts: # Loop through the parts of the response
  if part.text is not None: # If the part is text
    print(part.text)
  elif part.inline_data is not None: # If the part is an image
    # Save the image
    image_number = len(os.listdir("generated_images/")) + 1 # Counts how many images are there
    image = Image.open(BytesIO(part.inline_data.data))
    image.save(f"generated_images/image_{image_number}.png")
    print(f"[ generated_images/image_{image_number}.png ] - Generated Image")
    print()