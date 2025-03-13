from google import genai
import os

# Your Messages to the AI
prompt1 = "I have 2 dogs in my house."
prompt2 = "How many paws are in my house?"

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Create a chat
chat = client.chats.create(model="gemini-2.0-flash")

response = chat.send_message_stream(prompt1) # Send the first message

print("First response: ")

for chunk in response: # Collect the response
    print(chunk.text, end="") # Print the first response in chunks

response = chat.send_message_stream(prompt2) # Send the second message

print("\nSecond response: ")

for chunk in response: # Collect the second response
    print(chunk.text, end="") # Print the second response in chunks

print("\n-----------------\n\nChat history: ", end="") # Print a divider

# Print the chat history
for message in chat._curated_history:
    if message.role == "model":
        if not model_generated:
            print(f'role - ', message.role, end=": ")
        print(message.parts[0].text, end="")
        model_generated = True
    elif message.role == "user":
        print("\n") # Print a newline
        print(f'role - ', message.role, end=": ")
        print(message.parts[0].text)
        model_generated = False