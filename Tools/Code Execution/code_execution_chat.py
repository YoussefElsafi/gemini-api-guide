from google import genai
from google.genai import types
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# System Instruction | The instructions for the model.
system_instruction="""
  You are an expert software developer and a helpful coding assistant.
  You are able to generate high-quality code in any programming language.
"""

# Create a chat
chat = client.chats.create(
  model="gemini-2.0-flash", # The AI Model that we are gonna use
  config=types.GenerateContentConfig( # The configuration for the model
      system_instruction=system_instruction, # The system instruction for the model
      tools=[types.Tool( # The tool for code execution
          code_execution=types.ToolCodeExecution # Enabling The code execution tool
          )
    ]
)
)

# Generate the response
response = chat.send_message((
    'What is the sum of the first 50 prime numbers? '
    'Generate and run code for the calculation, and make sure you get all 50.'))

# Process the response to extract the text or code execution result
if hasattr(response, 'candidates') and response.candidates:
    for candidate in response.candidates:
        if hasattr(candidate.content, 'parts') and candidate.content.parts:
            for part in candidate.content.parts:
                if part.text:
                    print(part.text)
                elif hasattr(part, 'executable_code') and part.executable_code:
                    print(f"Executable Code: {part.executable_code.code}")
                elif hasattr(part, 'code_execution_result') and part.code_execution_result:
                    print(f"Code Execution Result: {part.code_execution_result.output}")
                else:
                    print(f"Unknown part type: {type(part)}")
        else:
            print("No parts in the response candidate.")
else:
    print("No candidates in the response.")