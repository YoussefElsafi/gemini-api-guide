# Gemini API: Text Generation - Detailed Guide

## Overview

This document provides a comprehensive guide on using the Gemini API for text generation. The Gemini API can generate text from various input types, including text, images, video, and audio. This guide focuses on text generation using the `generateContent` and `streamGenerateContent` methods with text-only and text-and-image inputs. Also included is a discussion on how to use and customize a chat conversation, and configure text generation through prompts, system instructions and more.

## Key Capabilities

-   **Text Generation:** Generate text from various inputs.
-   **Multimodal Inputs:** Combine text and media files (images, video, audio).
-   **Streaming:** Handle partial results for faster interactions using `streamGenerateContent`.
-   **Chat Conversations:** Maintain conversation history with the Gemini SDK's chat interface.
-   **Configurable Generation:** Control response generation with parameters like `max_output_tokens` and `temperature`.
-   **System Instructions:** Steer model behavior with specific instructions and guidelines.

## 1. Generate Text from Text-Only Input

-   Use the `generateContent` method to generate text from a text-only input.
-   This approach does not include examples, system instructions, or formatting information (zero-shot approach).

### Code Example (Python):

```python
from google import genai

client = genai.Client(api_key="GEMINI_API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["How does AI work?"])
print(response.text)
```

## 2. Generate Text from Text-and-Image Input

-   The Gemini API supports multimodal inputs that combine text and media files.

### Code Example (Python):

```python
from PIL import Image
from google import genai

client = genai.Client(api_key="GEMINI_API_KEY")

image = Image.open("/path/to/organ.png")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[image, "Tell me about this instrument"])
print(response.text)
```

-   Replace `/path/to/organ.png` with the actual path to your image file.
-   Make sure that you have the Pillow library installed if you want to use images, and if not install with the command, `pip install Pillow`.

## 3. Generate a Text Stream

-   Use the `streamGenerateContent` method to handle partial results for faster interactions.
-   Useful when you don't want to wait for the entire text generation process to complete before displaying the output.

### Code Example (Python):

```python
from google import genai

client = genai.Client(api_key="GEMINI_API_KEY")

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=["Explain how AI works"])
for chunk in response:
    print(chunk.text, end="")
```

## 4. Create a Chat Conversation

-   The Gemini SDK lets you collect multiple rounds of questions and responses to create a conversational history.
-   The `chats.create` method provides an interface to keep track of conversation history.
-   Behind the scenes, it uses the same `generateContent` method to create the response.

### Code Example (Python):

```python
from google import genai

client = genai.Client(api_key="GEMINI_API_KEY")

chat = client.chats.create(model="gemini-2.0-flash")
response = chat.send_message("I have 2 dogs in my house.")
print(response.text)
response = chat.send_message("How many paws are in my house?")
print(response.text)
for message in chat._curated_history:
    print(f'role - ', message.role, end=": ")
    print(message.parts[0].text)
```

-   The `_curated_history` attribute is a list of `Message` objects, each containing the `role` (either "user" or "model") and `parts` (the content of the message).

## 5. Streaming With Chat

-   You can also use streaming to generate text and have a conversation.

### Code Example (Python):

```python
from google import genai

client = genai.Client(api_key="GEMINI_API_KEY")

chat = client.chats.create(model="gemini-2.0-flash")
response = chat.send_message_stream("I have 2 dogs in my house.")
for chunk in response:
    print(chunk.text, end="")
response = chat.send_message_stream("How many paws are in my house?")
for chunk in response:
    print(chunk.text, end="")
for message in chat._curated_history:
    print(f'role - ', message.role, end=": ")
    print(message.parts[0].text)
```

## 6. Configure Text Generation

-   Control how the model generates responses using the `GenerationConfig` class.
-   If you don't configure the parameters, the model uses default options, which can vary by model.

### Code Example (Python):

```python
from google import genai
from google.genai import types

client = genai.Client(api_key="GEMINI_API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Explain how AI works"],
    config=types.GenerateContentConfig(
        max_output_tokens=500,
        temperature=0.1
    )
)
print(response.text)
```

-   `max_output_tokens`: Limits the length of the generated text.
-   `temperature`: Controls the randomness of the output. Lower values (e.g., 0.1) make the output more deterministic, while higher values (e.g., 0.9) make it more random.

## 7. Add System Instructions

-   Steer the behavior of a model based on your specific needs and use cases.
-   Provide additional context to understand the task and generate customized responses.
-   Specify product-level behavior by setting system instructions, separate from user prompts.

### Code Example (Python):

```python
sys_instruct="You are a cat. Your name is Neko."
client = genai.Client(api_key="GEMINI_API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction=sys_instruct),
    contents=["your prompt here"]
)
```

-   `system_instruction` is added to the config and is applied.

## What's Next

-   **Vision understanding:** Learn how to use Gemini's native vision understanding to process images and videos.
-   **Audio understanding:** Learn how to use Gemini's native audio understanding to process audio files.

This guide provides a foundation for text generation with the Gemini API. Remember to handle errors gracefully and be aware of the limitations of large language models.