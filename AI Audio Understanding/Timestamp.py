# Note: Gemini isn't always accurate at transcribing audio speech between timestamps.

import os
from google import genai

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

myfile = client.files.upload(file='Audios/Long_Speech.wav') # Upload the audio file to Gemini

# Generate the response
response = client.models.generate_content(
  model='gemini-2.0-pro-exp', # The recommended AI Model for this task
  contents=[
    'Provide a transcript of the speech from 0:20 to 0:27.', # The input prompt to the AI
    myfile, # The audio file that was uploaded
  ]
)

# Print the response
print(response.text)