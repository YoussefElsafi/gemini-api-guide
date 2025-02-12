from google import genai
from google.genai import types
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Generate the response
response = client.models.generate_content(
  model='gemini-2.0-flash', # The AI Model that we are gonna use
  contents='What is the sum of the first 50 prime numbers? ' # The first input prompt to the AI
           'Generate and run code for the calculation, and make sure you get all 50.', # The second input prompt to the AI
  config=types.GenerateContentConfig( # The configuration for the model
    tools=[types.Tool( # The tool for code execution
      code_execution=types.ToolCodeExecution # Enabling The code execution tool
    )]
  )
)
def print_code_execution_result(response):
    """
    Prints the code execution result from the response.

    It iterates over all candidates and parts of their content,
    printing text, code, output, and inline data when available.
    """
    if hasattr(response, 'candidates') and response.candidates:
        for candidate in response.candidates:
            if hasattr(candidate.content, 'parts') and candidate.content.parts:
                for part in candidate.content.parts:
                    if hasattr(part, 'text') and part.text:
                        print(part.text)
                    if hasattr(part, 'executable_code') and part.executable_code:
                        print(f"Executable Code: {part.executable_code.code}")
                    if hasattr(part, 'code_execution_result') and part.code_execution_result:
                        print(f"Code Execution Result: {part.code_execution_result.output}")
                    if hasattr(part, 'inline_data') and part.inline_data:
                        print(f"Inline Data: {part.inline_data.data[:50]}...")  # Displaying only first 50 characters for brevity
            else:
                print("No parts in this candidate's content.")
    else:
        print("No candidates found in the response.")

print_code_execution_result(response)