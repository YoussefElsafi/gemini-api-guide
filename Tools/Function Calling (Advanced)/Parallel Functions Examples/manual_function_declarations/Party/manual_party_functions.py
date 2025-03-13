from google import genai  # Import the Google Generative AI library
import os  # Import the operating system module
from google.genai import types  # Import specific types from the genai library

# Retrieve the API key from environment variables
API_KEY = os.environ["API_KEY"]
# Initialize the Generative AI client with the API key
client = genai.Client(api_key=API_KEY)

def power_disco_ball(power: bool) -> bool:
    """Powers the spinning disco ball."""
    print(f"Disco ball is {'spinning!' if power else 'stopped.'}")
    return True

def start_music(energetic: bool, loud: bool) -> str:
    """Play some music matching the specified parameters."""
    print(f"Starting music! {energetic=} {loud=}")
    return "Never gonna give you up."

def dim_lights(brightness: float) -> bool:
    """Dim the lights."""
    print(f"Lights are now set to {brightness:.0%}")
    return True

# Define the tool with manual function declarations.
tool_manual = types.Tool(
    function_declarations=[  # List of function declarations
        types.FunctionDeclaration(  # Declaration for power_disco_ball
            name="power_disco_ball",
            description="Powers the spinning disco ball.",
            parameters=types.Schema(
                properties={  # Parameter definition
                    'power': types.Schema(type=types.Type.BOOLEAN, description="Whether to turn the disco ball on (True) or off (False).")
                },
                type=types.Type.OBJECT,  # Parameters are an object
                required=['power']  # 'power' is a required parameter
            ),
        ),
        types.FunctionDeclaration(  # Declaration for start_music
            name="start_music",
            description="Play some music matching the specified parameters.",
            parameters=types.Schema(
                properties={
                    'energetic': types.Schema(type=types.Type.BOOLEAN, description="Whether the music should be energetic."),
                    'loud': types.Schema(type=types.Type.BOOLEAN, description="Whether the music should be loud.")
                },
                type=types.Type.OBJECT,
                required=['energetic', 'loud']
            ),
        ),
        types.FunctionDeclaration(  # Declaration for dim_lights
            name="dim_lights",
            description="Dim the lights.",
            parameters=types.Schema(
                properties={
                    'brightness': types.Schema(type=types.Type.NUMBER, description="The brightness level (0.0 to 1.0).")
                },
                type=types.Type.OBJECT,
                required=['brightness']
            ),
        )
    ]
)

# Create the configuration for function calling
config = {
    'tools': [tool_manual],  # Include the manually defined tool
}

# Create a chat session with the specified model and configuration
chat = client.chats.create(model='gemini-2.0-flash', config=config)
# Send a message to the model, triggering function calls
response = chat.send_message("Turn this place into a party!")

# Process the response from the model
if response.candidates:
    responses_to_send = []  # Initialize list to handle parallel function calls

    # Iterate through the candidates in the response
    for candidate in response.candidates:
        if candidate.content and candidate.content.parts:
            # Iterate through the parts of the candidate's content
            for part in candidate.content.parts:
                if part.text:
                    print(part.text)  # Print any text parts
                # Check if the part is a function call
                elif hasattr(part, 'function_call') and part.function_call:
                    func_call = part.function_call  # Extract the function call
                    print(f"Function Call: {func_call.name}({func_call.args})")  # Print the function call details

                    #  Handle each possible function call
                    if func_call.name == "power_disco_ball":
                        result = power_disco_ball(**{k: v for k, v in func_call.args.items()})
                    elif func_call.name == "start_music":
                        result = start_music(**{k: v for k, v in func_call.args.items()})
                    elif func_call.name == "dim_lights":
                        result = dim_lights(**{k: v for k,v in func_call.args.items()})
                    # Create a dictionary containing the result.  Important for the API.
                    response_dict = {"result": result}

                    # Accumulate function responses in case of parallel calls
                    responses_to_send.append(types.Part(function_response=types.FunctionResponse(name=func_call.name, response=response_dict)))

                # Check if the part is a function response
                elif hasattr(part, "function_response") and part.function_response:
                    print(f"Function response: {part.function_response}")  # Print function responses
    # Handle parallel function calls
    if responses_to_send:
        response2 = chat.send_message(responses_to_send)  # Send all function responses at once
        print(response2.text) # Print the models response.

# Handle the case where no candidates are returned
else:
    print("No candidates")