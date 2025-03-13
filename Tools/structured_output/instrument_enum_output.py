from google import genai
import enum
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)


# Enum class for musical instruments
class Instrument(enum.Enum):
    # Percussion instruments, e.g., drums
    PERCUSSION = "Percussion"
    # String instruments, e.g., guitar
    STRING = "String"
    # Woodwind instruments, e.g., flute
    WOODWIND = "Woodwind"
    # Brass instruments, e.g., trumpet
    BRASS = "Brass"
    # Keyboard instruments, e.g., piano
    KEYBOARD = "Keyboard"

# Generate the response
response = client.models.generate_content(
    model='gemini-2.0-flash',  # The AI Model
    contents='What type of instrument is an oboe?',  # The input prompt to the AI
    config={  # Model configuration
        'response_mime_type': 'text/x.enum',  # The response type
        'response_schema': {
            "type": "string",  # Specify the type as string
            "enum": [
                member.value for member in Instrument  # The enum values
            ]  # The enum schema
        },  # The response schema
    },
)

# Print the response
print(response.text)

# Correct answer: Woodwind