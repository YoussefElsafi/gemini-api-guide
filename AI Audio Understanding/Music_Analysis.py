import os
from google import genai

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

myfile = client.files.upload(file='Audios/Sample.mp3') # Upload the audio file to Gemini

# Generate the response
response = client.models.generate_content(
  model='gemini-2.0-flash', # The AI Model
  contents=[
    'Describe this audio clip', # The input prompt to the AI
    myfile, # The audio file that was uploaded
  ]
)

# Print the response
print(response.text)