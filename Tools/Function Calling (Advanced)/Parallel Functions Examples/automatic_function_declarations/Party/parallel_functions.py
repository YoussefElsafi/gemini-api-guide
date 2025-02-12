from google import genai  # Import the Google Generative AI library
import os  # Import the operating system module
from google.genai import types  # Import specific types from the genai library
import inspect  # Import the inspect module for function introspection

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

# List of functions that can be called by the model
house_fns = [power_disco_ball, start_music, dim_lights]

def create_function_declaration(fn):
    """Creates a FunctionDeclaration from a function."""
    param_schemas = {}  # Initialize an empty dictionary to store parameter schemas
    required_params = []  # Initialize an empty list to store required parameter names

    # Iterate through the parameters of the input function
    for param_name, param in inspect.signature(fn).parameters.items():
        # Check if the parameter is positional or keyword (i.e., not *args or **kwargs)
        if param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
            required_params.append(param_name)  # Add the parameter name to the required list
            param_type = param.annotation  # Get the type annotation of the parameter

            # Map Python type annotations to Gemini API schema types
            if param_type == bool:
                schema_type = types.Type.BOOLEAN  # Map bool to BOOLEAN
            elif param_type == str:
                schema_type = types.Type.STRING  # Map str to STRING
            elif param_type in (int, float):
                schema_type = types.Type.NUMBER  # Map int and float to NUMBER
            else:  # Fallback, you might need to add more specific types here
                schema_type = types.Type.OBJECT  # Default to OBJECT for unknown types

            # Create a schema for the current parameter
            param_schemas[param_name] = types.Schema(type=schema_type)


    # Create and return the FunctionDeclaration object
    return types.FunctionDeclaration(
        name=fn.__name__,  # Set the name of the function
        description=fn.__doc__,  # Set the description from the function's docstring
        parameters=types.Schema(  # Define the parameters schema
            type=types.Type.OBJECT,  # Parameters are represented as an object
            properties=param_schemas,  # Set the properties (individual parameters)
            required=required_params,  # Set the list of required parameters
        ),
    )


# Create the configuration for function calling
config = {
    'tools': [  # Define the available tools (functions)
        types.Tool(function_declarations=[  # Define the function declarations
            create_function_declaration(fn) for fn in house_fns  # Create declarations for each function
        ])
    ],
    'tool_config': {'function_calling_config': {'mode': 'ANY'}}  # Allow the model to call any function
}


# Create a chat session with the specified model and configuration
chat = client.chats.create(model='gemini-2.0-flash', config=config)
# Send a message to the model, prompting it to use function calling
response = chat.send_message('Turn this place into a party!')

# Iterate through the parts of the response
for part in response.candidates[0].content.parts:
    # Check if the current part represents a function call
    if hasattr(part, "function_call"):
        fn_call = part.function_call  # Get the function call object
        # Format the arguments as a string
        args_str = ", ".join(f"{k}={v}" for k, v in fn_call.args.items())
        # Print the function call in the format: function_name(arg1=val1, arg2=val2, ...)
        print(f"{fn_call.name}({args_str})")