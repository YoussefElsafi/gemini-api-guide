from google import genai
import io
import httpx
import os

# Prompt
prompt = "Summarize this document"

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# URL of the document
long_context_pdf_path = "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

sample_doc = client.files.upload(
  # You can pass a path or a file-like object here
  path=doc_io, 
  config=dict(
    # It will guess the mime type from the file extension, but if you pass
    # a file-like object, you need to set the
    mime_type='application/pdf')
)

# Generate the response
response = client.models.generate_content(
  model="gemini-2.0-flash", # The AI Model
  contents=[
      sample_doc, # The document
      prompt # The input prompt to the AI
  ]
)

# Print the response
print(response.text)