import os
from google import genai

# API Key
API_KEY = os.environ["API_KEY"] # Get the API key from the environment.
client = genai.Client(api_key=API_KEY) # Initialize the Gemini client.

print("Uploading file...")
video_file = client.files.upload(file="Videos/GreatRedSpot.mp4") # Upload the file.
print(f"Completed upload: {video_file.uri}") # Print the URI of the uploaded file.

# Pass the video file reference like any other media part.
response = client.models.generate_content(
    model="gemini-2.0-flash", # The model to use.
    contents=[
        video_file, # The video file.
        "Summarize this video. Then create a quiz with answer key " # The first message input part to the AI.
        "based on the information in the video." # The second message input part to the AI.
    ]
)

# Print the response
print("AI Response: ")
print(response.text) # Print the generated text.