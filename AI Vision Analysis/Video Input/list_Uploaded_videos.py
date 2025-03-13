from google import genai
import time
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

print("Uploading file...")
video_file = client.files.upload(file="Videos/GreatRedSpot.mp4") # Upload the file
print(f"Completed upload: {video_file.uri}")

print("Verifying Upload...")

# Check whether the file is ready to be used.
while video_file.state.name == "PROCESSING":
    print('.', end='')
    time.sleep(1)
    video_file = client.files.get(name=video_file.name) # Gets the uploaded file

if video_file.state.name == "FAILED":
  raise ValueError(video_file.state.name)

print('Done!\n')

print('My files:')
for f in client.files.list():
  print(" ", f'{f.name}: {f.uri}')

# Pass the video file reference like any other media part.
response = client.models.generate_content(
    model="gemini-2.0-flash", # The model
    contents=[
        video_file, # The video file
        "Summarize this video. Then create a quiz with answer key " # The first message input part to the AI
        "based on the information in the video." # The second message input part to the AI
    ]
)

# Print the response
print("AI Response: ")
print(response.text)