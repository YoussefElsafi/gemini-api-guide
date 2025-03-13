from google import genai
import os

# Prompt
prompt = "Summarize this document"

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Upload the document to Gemini
document = client.files.upload(file="Documents/PDF.pdf", config=dict(mime_type='application/pdf'))

# Generate the response
response = client.models.generate_content(
  model="gemini-2.0-flash", # The AI Model
  contents=[
      document, # The document
      prompt # The input prompt to the AI
  ]
)

# Print the response
print(response.text)