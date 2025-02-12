from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Model
model_id = "gemini-2.0-flash"

# Google Search Tool
google_search_tool = Tool(
    google_search = GoogleSearch()
)

# Generate the response
response = client.models.generate_content(
    model=model_id, # The AI Model
    contents="When is the next total solar eclipse in the United States?", # The input prompt to the AI
    config=GenerateContentConfig( # The configuration
        tools=[
            google_search_tool # Enabling The Google Search Retrieval tool
        ], # The tools
        response_modalities=["TEXT"], # The output response type
    )
)

print("Response: ")
# Print the response (Not the search data content)
for each in response.candidates[0].content.parts:
    print(each.text)
# Example response:
# The next total solar eclipse visible in the contiguous United States will be on ...

print("\nGrounding Metadata: ")
# To get grounding metadata as web content.
print(response.candidates[0].grounding_metadata.search_entry_point.rendered_content)