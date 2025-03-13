from google import genai
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Generate the response
response = client.models.generate_content(
    model='gemini-2.0-flash', # The AI Model
    contents='What type of instrument is an oboe?',
    config={ # Model configuration
        'response_mime_type': 'text/x.enum', # The response type
        'response_schema': { # The response schema
            "type": "STRING", # Specify the type as string
            "enum": [
                "Percussion",
                "String",
                "Woodwind",
                "Brass",
                "Keyboard"
            ], # The enum schema
        },
    },
)

# Print the response
print(response.text)

# Correct answer: Woodwind