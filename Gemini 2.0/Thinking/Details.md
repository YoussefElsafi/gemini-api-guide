--------------------------------------------------------------------------------

                Gemini API: Gemini 2.0 Flash Thinking Model

--------------------------------------------------------------------------------

OVERVIEW:

The Gemini 2.0 Flash Thinking model is an *experimental* model designed to reveal its "thinking process" during response generation. This leads to enhanced reasoning capabilities compared to the standard Gemini 2.0 Flash Experimental model.  The "thoughts" themselves are *not* returned by the Gemini API, only in Google AI Studio.

ACCESSING THE MODEL:

*   **Google AI Studio:** You can directly interact with the Flash Thinking model within Google AI Studio.
*   **Gemini API:** Access is available through the Gemini API.
    *   **Alias:** Use the alias `gemini-2.0-flash-thinking-exp` to automatically use the latest version of the Flash Thinking model.
    *   **Specific Version:**  You can also specify the full model name if you need a particular version.
    *   **API Version:**  Crucially, you must use the `v1alpha` version of the API.

USING THE MODEL (API - Python Example):

1.  **Install the SDK:**
    ```
    pip install -U google-genai
    ```

2.  **Set up the Client (v1alpha):**
    ```
    client = genai.Client(api_key=GOOGLE_API_KEY, http_options={'api_version':'v1alpha'})
    ```
    *   Notice the `http_options` setting to specify the `v1alpha` API version.

3.  **Send a Basic Request:**
    ```
    response = client.models.generate_content(model='gemini-2.0-flash-thinking-exp', contents='Your prompt here.')
    print(response.text)
    ```

MULTI-TURN CONVERSATIONS:

*   **No Access to Previous Thoughts:**  In multi-turn conversations, you must provide the *entire* conversation history with each request. The model does *not* automatically retain its previous "thoughts" from earlier turns.
*   **Using the `genai.Chat` Object (Recommended):** The `google-genai` SDK provides a `Chat` object to simplify managing the conversation state.

    ```python
    chat = client.aio.chats.create(model='gemini-2.0-flash-thinking-exp')
    response = await chat.send_message('First message')
    print(response.text)
    response = await chat.send_message('Second message')
    print(response.text)
    ```
    The `Chat` object handles sending the conversation history automatically.  This is much cleaner than manually managing the history.

LIMITATIONS (Experimental Model):

*   **Input:** Text and image input *only*.
*   **Output:** Text output *only*.
*   **No JSON Mode or Search Grounding:**  These features are not supported.
*   **Thoughts Visibility:** The model's "thoughts" are *only* visible in Google AI Studio.  The Gemini API does *not* return them.

KEY TAKEAWAYS:

*   The Flash Thinking model is experimental and focuses on enhanced reasoning.
*   You *must* use the `v1alpha` version of the Gemini API.
*   Manage conversation history carefully in multi-turn interactions.
*   Be aware of the input/output and feature limitations.
*   Use the `Chat` object for easier multi-turn conversation management.
* The model's name can be set as an alias or use a specific full name.

--------------------------------------------------------------------------------