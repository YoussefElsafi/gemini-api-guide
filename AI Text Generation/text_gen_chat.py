from google import genai
import os
# API Key
API_KEY = os.environ["API_KEY"]
# Your Messages to the AI
prompt1 = "I have 2 dogs in my house."
prompt2 = "How many paws are in my house?"

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Create a chat
chat = client.chats.create(model="gemini-2.0-flash")
response = chat.send_message(prompt1) # Send the first message
print(response.text) # Print the response
response = chat.send_message(prompt2) # Send the second message
print(response.text) # Print the second response

# Print the chat history
for message in chat._curated_history:
    print(f'role - ', message.role, end=": ")
    print(message.parts[0].text)