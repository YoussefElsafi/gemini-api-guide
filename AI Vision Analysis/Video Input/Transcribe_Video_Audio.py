from google import genai
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

print("Uploading file...")
video_file = client.files.upload(file="Videos/GreatRedSpot.mp4") # Upload the file
print(f"Completed upload: {video_file.uri}")

# Pass the video file reference like any other media part.
response = client.models.generate_content(
    model="gemini-2.0-flash", # The model
    contents=[
        video_file, # The video file
        "Transcribe the audio from this video, giving timestamps for " # The first message input part to the AI
        "salient events in the video. Also provide visual descriptions." # The second message input part to the AI
    ]
)

# Print the response
print("AI Response: ")
print(response.text)