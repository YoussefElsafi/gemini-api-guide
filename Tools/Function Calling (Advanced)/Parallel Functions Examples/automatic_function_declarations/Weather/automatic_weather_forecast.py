from google import genai
import os
from google.genai import types
import inspect

API_KEY = os.environ["API_KEY"]
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
    print(f"Getting weather for {city} in {unit}")
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


def create_function_declaration(fn):
    """Creates a FunctionDeclaration from a function."""
    param_schemas = {}
    required_params = []

    for param_name, param in inspect.signature(fn).parameters.items():
        if param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
            required_params.append(param_name)
            param_type = param.annotation

            if param_type == bool:
                schema_type = types.Type.BOOLEAN
            elif param_type == str:
                schema_type = types.Type.STRING
            elif param_type in (int, float):
                schema_type = types.Type.NUMBER
            else:
                schema_type = types.Type.OBJECT

            param_schemas[param_name] = types.Schema(type=schema_type)


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
                create_function_declaration(get_current_weather)
            ]
        )
    ],
}

chat = client.chats.create(model='gemini-2.0-flash', config=config)
response = chat.send_message("What's the weather like in London and New York?")

if response.candidates:
    responses_to_send = []  # Accumulate responses
    for candidate in response.candidates:
        if candidate.content and candidate.content.parts:
            for part in candidate.content.parts:
                if part.text:
                    print(part.text)
                elif hasattr(part, 'function_call') and part.function_call:
                    func_call = part.function_call
                    print(f"Function Call: {func_call.name}({func_call.args})")
                    if func_call.name == "get_current_weather":
                        result = get_current_weather(**{k: v for k, v in func_call.args.items()})
                        response_dict = {"result": result}
                        responses_to_send.append(types.Part(function_response=types.FunctionResponse(name=func_call.name, response=response_dict)))

                elif hasattr(part, "function_response") and part.function_response:
                    print(f"Function response: {part.function_response}")
    # Send all accumulated responses in a single turn
    if responses_to_send:
        response2 = chat.send_message(responses_to_send)
        print(response2.text)

else:
    print("No candidates")