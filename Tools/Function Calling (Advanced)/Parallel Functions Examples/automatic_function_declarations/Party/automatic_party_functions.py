from google import genai
import os
from google.genai import types
import inspect

API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

def power_disco_ball(power: bool) -> bool:
    """Powers the spinning disco ball."""
    print(f"Disco ball is {'spinning!' if power else 'stopped.'}")
    return True

def start_music(energetic: bool, loud: bool) -> str:
    """
    Play some music matching the specified parameters.
    """
    print(f"Starting music! {energetic=} {loud=}")
    return "Never gonna give you up."

def dim_lights(brightness: float) -> bool:
    """
    Dim the lights.
    """
    print(f"Lights are now set to {brightness:.0%}")
    return True

house_fns = [power_disco_ball, start_music, dim_lights]

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
                create_function_declaration(fn)
                for fn in house_fns
            ]
        )
    ],
}

chat = client.chats.create(model='gemini-2.0-flash', config=config)
response = chat.send_message('Do everything you need to turn this place into a party!')

# Correctly handle the response, including function calls, and respond to ALL calls
if response.candidates:
    responses_to_send = []  # List to accumulate responses
    for candidate in response.candidates:
        if candidate.content and candidate.content.parts:
            for part in candidate.content.parts:
                if part.text:
                    print(part.text)
                elif hasattr(part, 'function_call') and part.function_call:
                    func_call = part.function_call
                    print(f"Function Call: {func_call.name}({func_call.args})")

                    if func_call.name == "power_disco_ball":
                        result = power_disco_ball(**{k: v for k, v in func_call.args.items()})
                    elif func_call.name == "start_music":
                        result = start_music(**{k: v for k, v in func_call.args.items()})
                    elif func_call.name == "dim_lights":
                        result = dim_lights(**{k: v for k,v in func_call.args.items()})

                    response_dict = {"result": result}
                    # Accumulate responses, DO NOT send immediately
                    responses_to_send.append(types.Part(function_response=types.FunctionResponse(name=func_call.name, response=response_dict)))

                elif hasattr(part, "function_response") and part.function_response:
                    print(f"Function response: {part.function_response}")
    # Send ALL accumulated responses in ONE turn
    if responses_to_send:
        response2 = chat.send_message(responses_to_send)
        print(response2.text)
else:
    print("No candidates")