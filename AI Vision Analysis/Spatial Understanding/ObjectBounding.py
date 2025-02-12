from google import genai
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Your Message to the AI
prompt = (
  """
  Detect items, objects or animals, with no more than 20 items.
  Output a json list where each entry contains the 2D bounding box in "box_2d" and a text label in "label".
  """
)

# Image
img_path = "Images/Example_Image.png" # The path to the image
image = client.files.upload(file=img_path) # Upload the image to gemini

# Generate the response
response = client.models.generate_content(
  model="gemini-2.0-flash-exp", # The recommended AI model
  contents=[
    image, # The image
    prompt # The input message to the AI
  ]
)

# Print the response
print(response.text)