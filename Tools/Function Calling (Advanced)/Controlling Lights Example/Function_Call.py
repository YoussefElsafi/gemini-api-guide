from google import genai
import os
from google.genai import types

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

def set_light_values(brightness: int, color_temp: str) -> dict[str, int | str]:
    """Set the brightness and color temperature of a room light. (mock API)."""
    print(f"Setting brightness to {brightness} and color temp to {color_temp}")  # For demonstration
    return {
        "brightness": brightness,
        "colorTemperature": color_temp
    }

# Define the function schema for the model
config = {
    'tools': [types.Tool(function_declarations=[
        types.FunctionDeclaration( # Function declaration for setting light values
            name="set_light_values", # Function name
            description="Set brightness and color temp of a light.", # Function description
            parameters=types.Schema( # Function parameters
                type=types.Type.OBJECT, # Object type
                properties={ # Properties
                    "brightness": types.Schema(type=types.Type.INTEGER), # Brightness property
                    "color_temp": types.Schema(type=types.Type.STRING) # Color temperature property
                },
                required=["brightness", "color_temp"] # Required properties
            )
        )
    ])],
}

# Create a chat session
chat = client.chats.create(
    model='gemini-2.0-flash', # The AI Model
    config=config # The model configuration with the function schema
)


# Generate the response (first turn)
response = chat.send_message('Turn the lights down to a romantic level, like 20% brightness and warm color temp.')

# Process the response and handle function calls
if response.candidates:
    for candidate in response.candidates:
        if candidate.content and candidate.content.parts:
            for part in candidate.content.parts:
                if part.text:
                    print(part.text)
                elif hasattr(part, 'function_call') and part.function_call:
                    func_call = part.function_call
                    # Call the function and get the result
                    if func_call.name == "set_light_values":
                        args = {k: v for k, v in func_call.args.items()}  # Convert to dict

                        result = set_light_values(**args)

                        # Send the function response back (second turn)
                        func_response_part = types.Part(function_response=types.FunctionResponse(name=func_call.name, response=result))
                        response2 = chat.send_message(func_response_part)
                        print(response2.text)