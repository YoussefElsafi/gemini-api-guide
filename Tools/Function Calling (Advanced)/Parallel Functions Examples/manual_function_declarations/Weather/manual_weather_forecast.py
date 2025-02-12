from google import genai  # Import the Google Generative AI library
import os  # Import the operating system module
from google.genai import types  # Import specific types from the genai library

# Retrieve the API key from environment variables
API_KEY = os.environ["API_KEY"]
# Initialize the Generative AI client with the API key
client = genai.Client(api_key=API_KEY)

def get_current_weather(city: str, unit: str = "celsius") -> dict:
    """
    Gets the current weather for a given city.

    Args:
        city: The city to get the weather for.
        unit: The unit of temperature to use ("celsius" or "fahrenheit"). Defaults to "celsius".

    Returns:
        A dictionary containing the weather information.  Example: {"temperature": 25, "condition": "Sunny"}
    """
    unit = unit.lower() # make the unit lower case
    print(f"Getting weather for {city} in {unit}")  # Print a message indicating which city's weather is being retrieved
    #  Here you'd actually call a real weather API.  This is a placeholder.
    if city.lower() == "london":
      if unit == "celsius":
        return {"temperature": 15, "condition": "Cloudy"}
      else:
        return {"temperature": 59, "condition": "Cloudy"}
    elif city.lower() == "new york":
      if unit == "celsius":
          return {"temperature": 22, "condition": "Rainy"}
      else:
          return {"temperature": 72, "condition": "Rainy"}
    else:
        return {"temperature": 20, "condition": "Unknown"}

# Define the tool with manual function declarations
tool_manual = types.Tool(
    function_declarations=[  # Define the function declarations within the tool
        types.FunctionDeclaration(  # Define a single function declaration
            name="get_current_weather",  # Set the name of the function
            description="Gets the current weather for a given city.",  # Set the description of the function
            parameters=types.Schema(  # Define the parameters schema
                properties={  # Define the properties (parameters) of the function
                    'city': types.Schema(type=types.Type.STRING, description="The city to get the weather for."),  # Define the 'city' parameter
                    'unit': types.Schema(type=types.Type.STRING, description="The unit of temperature (celsius or fahrenheit)."),  # Define the 'unit' parameter with corrected defaultValue
                },
                type=types.Type.OBJECT,  # Parameters are represented as an object
                required=['city']  # Set the list of required parameters
            ),
        )
    ]
)

# Create the configuration for function calling
config = {
    'tools': [tool_manual],  # Add the defined tool to the configuration
}

# Create a chat session with the specified model and configuration
chat = client.chats.create(model='gemini-2.0-flash', config=config)
# Send a message to the model, prompting it to use function calling
response = chat.send_message("What is the weather like in London and New York?")

# Process the response from the model
if response.candidates:  # Check if there are any candidates in the response
    responses_to_send = []  # Initialize an empty list to handle parallel function calls

    # Iterate through the candidates in the response
    for candidate in response.candidates:
        # Check if the candidate has content and parts
        if candidate.content and candidate.content.parts:
            # Iterate through the parts of the content
            for part in candidate.content.parts:
                # Check if the part contains text
                if part.text:
                    print(part.text)  # Print the text content
                # Check if the part represents a function call
                elif hasattr(part, 'function_call') and part.function_call:
                    func_call = part.function_call  # Get the function call object
                    print(f"Function Call: {func_call.name}({func_call.args})")  # Print the function call details

                    # Check if the function call is for 'get_current_weather'
                    if func_call.name == "get_current_weather":
                        # Execute the function with the provided arguments
                        result = get_current_weather(**{k: v for k, v in func_call.args.items()})
                        response_dict = {"result": result}  # Create a dictionary with the result

                        # Accumulate Function Responses for Parallel Calls
                        responses_to_send.append(types.Part(function_response=types.FunctionResponse(name=func_call.name, response=response_dict)))

                # Check if the part represents a function response
                elif hasattr(part, "function_response") and part.function_response:
                    print(f"Function response: {part.function_response}")  # Print the function response details
    #Handling Parallel Function calls
    if responses_to_send:
        response2 = chat.send_message(responses_to_send)
        print(response2.text)

# If no candidates are found, print a message
else:
    print("No candidates")