from google import genai  # Import the Google Generative AI library
import os  # Import the operating system module
from google.genai import types  # Import specific types from the genai library

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

# Define the tool with manual function declarations
tool_manual = types.Tool(
    function_declarations=[  # Define the function declarations within the tool
        types.FunctionDeclaration(  # Define a single function declaration
            name="search_product",  # Set the name of the function
            description="Searches for products in a given category.",  # Set the description
            parameters=types.Schema(  # Define the parameters schema
                properties={  # Define the properties (parameters) of the function
                    'query': types.Schema(type=types.Type.STRING, description="The search query."),
                    'category': types.Schema(type=types.Type.STRING, description="The category to search in (e.g., electronics, books, clothing, all). Defaults to all."),
                },
                type=types.Type.OBJECT,  # Parameters are represented as an object
                required=['query']  # Only query is required
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
response = chat.send_message("Search for laptops in electronics and mystery books.")

# Process the response from the model
if response.candidates:  # Check if there are any candidates in the response
    responses_to_send = [] # handle Parallel calls

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
                        # accumulate to handle parallel calls.
                        responses_to_send.append(types.Part(function_response=types.FunctionResponse(name=func_call.name, response=response_dict)))

                elif hasattr(part, "function_response") and part.function_response:
                    print(f"Function response: {part.function_response}")
    # Handle parallel function calls
    if responses_to_send:
        response2 = chat.send_message(responses_to_send) #send all calls at once
        print(response2.text) # prints the Model response

# If no candidates are found, print a message
else:
    print("No candidates")