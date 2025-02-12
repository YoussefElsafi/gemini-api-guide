from google import genai  # Import the Google Generative AI library
import os  # Import the operating system module
from google.genai import types  # Import specific types from the genai library
import inspect  # Import the inspect module for function introspection

# Retrieve the API key from environment variables
API_KEY = os.environ["API_KEY"]
# Initialize the Generative AI client with the API key
client = genai.Client(api_key=API_KEY)

def search_product(query: str, category: str = "all") -> list:
    """
    Searches for products in a given category.

    Args:
        query: The search query.
        category: The category to search in (e.g., "electronics", "books", "clothing", "all"). Defaults to "all".

    Returns:
        A list of product names. Example: ["Product A", "Product B"]
    """
    print(f"Searching for {query} in {category}")

    # This is a placeholder.  Replace with a real e-commerce API call.
    if query.lower() == "laptop" and category.lower() == "electronics":
        return ["Laptop Model X", "Laptop Model Y", "Laptop Model Z"]
    elif query.lower() == "mystery" and category.lower() == "books":
        return ["The Silent Patient", "Gone Girl", "The Guest List"]
    else:
        return ["No products found."]

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
            else:
                schema_type = types.Type.OBJECT  # Map other types to OBJECT

            # Create a schema for the current parameter
            param_schemas[param_name] = types.Schema(type=schema_type)

    # Return FunctionDeclaration.
    return types.FunctionDeclaration(
        name=fn.__name__,
        description=fn.__doc__,
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties=param_schemas,
            required=required_params,
        ),
    )

config = {
    'tools': [
        types.Tool(
            function_declarations=[
                create_function_declaration(search_product) # Automatically generate declaration
            ]
        )
    ],
}

# Create a chat session using the Gemini model and the configuration
chat = client.chats.create(model='gemini-2.0-flash', config=config)
# Send a message to initiate the conversation and trigger function calling
response = chat.send_message("Search for laptops in electronics and mystery books.")

if response.candidates:
    responses_to_send = [] # Handle parallel function calls

    for candidate in response.candidates:
        if candidate.content and candidate.content.parts:
            for part in candidate.content.parts:
                if part.text:
                    print(part.text)
                elif hasattr(part, 'function_call') and part.function_call:
                    func_call = part.function_call
                    print(f"Function Call: {func_call.name}({func_call.args})")
                    if func_call.name == "search_product":
                        result = search_product(**{k: v for k, v in func_call.args.items()})
                        response_dict = {"result": result}
                        # Accumulate responses in the case of parallel calls
                        responses_to_send.append(types.Part(function_response=types.FunctionResponse(name=func_call.name, response=response_dict)))

                elif hasattr(part, "function_response") and part.function_response:
                    print(f"Function response: {part.function_response}")

    # If there are responses to send, send them all at once (parallel function call handling)
    if responses_to_send:
      response2 = chat.send_message(responses_to_send)
      print(response2.text)

else:
    print("No candidates")