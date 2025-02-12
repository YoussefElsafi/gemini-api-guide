from google import genai
from google.genai import types
import httpx
import os

# Prompt
prompt = "Summarize this document"

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# URL of the document
doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"

# Retrieve and encode the document as bytes
doc_data = httpx.get(doc_url).content

# Generate the response
response = client.models.generate_content(
  model="gemini-2.0-flash", # The AI Model
  contents=[
      types.Part.from_bytes( # Create a Part object from bytes
        data=doc_data, # The document data
        mime_type='application/pdf', # The MIME type of the document
      ), # The document
      prompt # The input prompt to the AI
  ]
)

# Print the response
print(response.text)