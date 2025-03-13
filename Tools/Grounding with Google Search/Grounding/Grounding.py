from google import genai
from google.genai import types
import os

# Prompt
prompt = "Who won Wimbledon this year?"

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Generate the response
response = client.models.generate_content(
    model='gemini-2.0-flash', # The AI Model
    contents=prompt, # The input prompt to the AI
    config=types.GenerateContentConfig( # The configuration
        tools=[types.Tool( # The tools
            google_search=types.GoogleSearchRetrieval # The Google Search Retrieval tool
        )]
    )
)

# Print the response
print(response.text)