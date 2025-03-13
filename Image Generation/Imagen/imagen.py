from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Generate the image
response = client.models.generate_images(
    model='imagen-3.0-generate-002', # The Image Generation Model
    prompt='Fuzzy bunnies in my kitchen', # The input prompt to Imagen
    config=types.GenerateImagesConfig( # The configuration for the image generation
        number_of_images= 1, # The number of images to generate
    )
)

# Display the generated images
for generated_image in response.generated_images:
  image = Image.open(BytesIO(generated_image.image.image_bytes))
  image.show()