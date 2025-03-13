--------------------------------------------------------------------------------

               Gemini API: Function Calling (Detailed Guide)

--------------------------------------------------------------------------------

OVERVIEW:

Function calling allows Gemini models to interact with *external systems and APIs*.  You provide descriptions of functions (written in *your* application's code, *not* Google Cloud Functions), and the model can predict when to call those functions and with what arguments.  The model does *not* directly execute the functions; it provides structured output (JSON) that you use to call the function.  This allows you to integrate real-time data and services into the model's responses.

KEY CONCEPTS:

*   **Function Declarations:**  Structured descriptions (using a subset of the OpenAPI schema) of the functions your application can perform.  These tell the model the function's name, purpose, parameters, and parameter types.
*   **Model Prediction:** The model analyzes your prompt and the function declarations.  It then predicts:
    *   *Which* function (if any) should be called.
    *   The *arguments* to pass to that function.
*   **Your Application's Role:**  Your application receives the model's predicted function call (name and arguments), *executes* the actual function (calling external APIs or services as needed), and then sends the *result* back to the model.
*   **Iterative Process:** The model can then use the function's result to generate a more informed and accurate response to the user's original query.  This can be a multi-turn process.
* **Best Use:** Is best for interacting with external systems, instead code execution should be used for computation.

FUNCTION DECLARATIONS (Structure):

You define function declarations within a `tools` object in your API request.  Each declaration includes:

*   **`name` (string, required):**  A unique identifier for the function (no spaces, periods, or dashes; use underscores or camelCase).
*   **`description` (string, required):** A clear, detailed explanation of the function's purpose.  Be specific and provide examples if needed.
*   **`parameters` (object, required):**  Defines the input data the function needs.
    *   **`type` (string, required):**  The overall data type of the parameters (usually `"object"`).
    *   **`properties` (object, required):**  Describes each individual parameter:
        *   **`type` (string, required):** The data type of the parameter (`"string"`, `"integer"`, `"number"`, `"boolean"`, `"array"`, `"object"`).  Use strong types.
        *   **`description` (string, required):**  A clear explanation of the parameter's purpose and expected format/values.  Give examples.
        *   **`enum` (array, optional):** If the parameter has a limited set of valid values, use an `enum` to list them.
    *   **`required` (array, optional):**  A list of the names of parameters that are *required* for the function to work.

BEST PRACTICES (Function Declarations):

*   **Clear Names:**  Use descriptive names without spaces, periods, or dashes.
*   **Detailed Descriptions:** Be very specific about what the function does.  Give examples.  Don't be ambiguous.
*   **Strong Types:** Use the most specific `type` possible (e.g., `integer` instead of `number`). Use `enum` when appropriate.
*   **Example Values:**  In parameter descriptions, provide concrete examples of valid values and constraints.

FUNCTION CALLING MODES:

The `function_calling_config` object (within `tool_config`) controls how the model uses functions:

*   **`mode` (string):**
    *   **`"AUTO"` (Default):**  The model decides whether to call a function or respond with natural language.
    *   **`"ANY"`:**  Forces the model to *always* predict a function call.
    *   **`"NONE"`:**  Prevents the model from predicting any function calls.
*   **`allowed_function_names` (array of strings, optional):**  When `mode` is `"ANY"`, this limits the model to choosing from the specified functions.  If not provided (with `"ANY"`), the model can choose from *all* declared functions.

COMPOSITIONAL FUNCTION CALLING (Gemini 2.0):

*   **Multiple Functions:** Gemini 2.0 can invoke *multiple* functions in a single response to handle complex requests.
*   **Example:**  For "Get the temperature in my current location," the model might call `get_current_location()` and then `get_weather(location)`.
* **Requires:** Bidirectional streaming and the Multimodal Live API.

MULTI-TOOL USE:

*  **Multiple Tools:** Gemini 2.0 models support enabling various tools, letting the model decide.
*  **Example:** You could enable Google Search, code execution, and function calling, simultaneously.
*  **Supported Models:** The Multimodal Live API.

FUNCTION CALLING EXAMPLES (cURL):

The documentation provides example cURL requests demonstrating:

*   **Single-Turn:**  The model predicts a function call based on a single prompt.
*   **Multi-Turn:**  The user sends the function's result back to the model for a more complete response.
*   **Different Modes:**  Using `"AUTO"`, `"ANY"`, and `"ANY"` with `allowed_function_names`.

BEST PRACTICES (Overall):

*   **User Prompt:**
    *   Provide context: Explain the role of the model (e.g., "You are a movie API assistant...").
    *   Give instructions:  Tell the model how and when to use functions.
    *   Encourage clarification:  Instruct the model to ask clarifying questions if the user's request is ambiguous.
*   **Sampling Parameters:** Use a low `temperature` (e.g., 0) for more deterministic and reliable function call predictions.
*   **API Invocation:**
    *   *Validate* the model's predicted function call and arguments *before* executing any function that has significant consequences (e.g., placing an order, updating a database).
    *   Consider getting user confirmation before executing such functions.

FUNCTION CALLING DATA TYPE MAPPING

* **Allowed Types:** Are int, float, bool, str, list['AllowedType'], dict[str, AllowedType].
* **SDK Conversion:** The SDK converts function parameter type annotations to a format the API understands.

PYTHON SDK SPECIFIC NOTES:

*   **Automatic Function Calling:** The Python SDK, by default, *automatically* calls the functions predicted by the model and sends the results back.
*   **Disabling Automatic Calling:** You can disable this with `automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)` in the `GenerateContentConfig`.  This gives you more control over the process.
*   **Parallel Function Calling:**  The Python SDK supports calling multiple functions in a single turn.  You can iterate through the `response.function_calls` to see the predicted calls.
*   **Error Handling (Automatic Calling):**  If a function call fails, the SDK passes the error back to the model, which may try again (potentially with corrected arguments).  Be careful with functions that have side effects.
*   **Schema Definition:**  You can define function schemas using:
    *   **Python Function Annotations (Limited):**  The SDK can infer a schema from a Python function's type annotations, but this has limitations (e.g., it doesn't handle nested dictionaries well).
    *   **`genai.types.FunctionDeclaration` (More Control):**  You can explicitly define the schema using `genai.types.FunctionDeclaration` and related classes.  This gives you full control and allows you to define schemas for non-Python functions (e.g., wrapping HTTP calls).

This enhanced `details.md` provides a comprehensive and detailed explanation of function calling with the Gemini API, covering the core concepts, best practices, different modes, advanced features (compositional calling, multi-tool use), and specifics of using the Python SDK. It's suitable for developers who want to deeply understand how to integrate function calling into their applications. It also distinguishes the capabilities between Gemini 1.5 and Gemini 2.0 models.