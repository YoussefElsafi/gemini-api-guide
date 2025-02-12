import os
from google import genai
from google.genai import types  # Added for handling file parts

# API Key
API_KEY = os.environ["API_KEY"] # Get API key from environment variable
client = genai.Client(api_key=API_KEY) # Initialize the Gemini client

with open('Audios/Sample.mp3', 'rb') as f: # Open the audio file in binary read mode
    audio_bytes = f.read() # Read the audio file

# Generate the response
response = client.models.generate_content(
  model='gemini-2.0-flash', # The AI Model to use
  contents=[ # The contents for the model
    'Describe this audio clip', # Prompt for the model
    types.Part.from_bytes( # Create a Part object from bytes
      data=audio_bytes, # The audio data
      mime_type='audio/mp3', # The MIME type of the audio
    )
  ]
)

print(response.text) # Print the model's response