import time
import os
from google import genai

# API Key
API_KEY = os.environ["API_KEY"] # Get the API key from the environment.
client = genai.Client(api_key=API_KEY) # Initialize the Gemini client.

print("Uploading file...")
video_file = client.files.upload(file="Videos/Example_Video.mp4") # Upload the file.
print(f"Completed upload: {video_file.uri}") # Print the URI of the uploaded file.

print("Verifying Upload...")

# Check whether the file is ready to be used.
while video_file.state.name == "PROCESSING": # Loop until the file is processed.
    print('.', end='') # Print a dot to show progress.
    time.sleep(1) # Wait for 1 second.
    video_file = client.files.get(name=video_file.name) # Gets the uploaded file to check its status.

if video_file.state.name == "FAILED": # Check if the upload failed.
  raise ValueError(video_file.state.name) # Raise an error if the upload failed.

print('Verified!\n')