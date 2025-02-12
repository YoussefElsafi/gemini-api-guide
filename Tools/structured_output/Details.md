--------------------------------------------------------------------------------

                      Gemini API: Generating Structured Output (JSON & Enums)

--------------------------------------------------------------------------------

OVERVIEW:

The Gemini API typically generates unstructured text.  However, many applications need structured data, like JSON, for easier processing.  This document describes how to constrain the Gemini API to produce JSON output or to select from a predefined set of options using enums.

USE CASES (for structured output):

*   **Data Extraction:**  Pull structured information from unstructured sources (e.g., extracting company details from news articles, standardizing resume data, extracting ingredients from recipes).
*   **Database Creation:**  Build databases by extracting and organizing information.
*   **Integration with Other Systems:**  JSON is a common format for exchanging data between systems, making integration easier.

GENERATING JSON OUTPUT:

You can prompt Gemini to output JSON, but it's not guaranteed to be *exclusively* JSON.  For more reliable and predictable results, you should provide a JSON schema.  There are two main methods:

1.  **Schema as Text in Prompt:**

    *   Include the desired JSON structure as text within your prompt.  This offers flexibility in how you represent the schema.
    *   Example (Illustrative):
        ```
        "Use this JSON schema:  Recipe = {'recipe_name': str, 'ingredients': list[str]}  Return: list[Recipe]"
        ```
        The prompt specifies the expected structure.

2.  **Schema via Model Configuration (More Precise Control):**

    *   This is the recommended approach for greater control and predictability.  You provide a structured schema as part of the model's configuration.
    *   Example (Illustrative):
        ```
        config={'response_mime_type': 'application/json', 'response_schema': list[Recipe]}
        ```
        This sets the `response_mime_type` to `application/json` and defines the `response_schema`.

SCHEMA DEFINITION SYNTAX:

You define the JSON schema in the `response_schema` property of the model configuration.  The value of `response_schema` can be:

*   **A Type (like in type annotations):** The easiest method.  Uses Python typing constructs.
*   **An Instance of `genai.types.Schema`:** A more explicit, Gemini API-specific way.
*   **A Dictionary Equivalent of `genai.types.Schema`:**  Similar to the above, but using a standard Python dictionary.

SUPPORTED TYPES (for schema definition):

The Gemini API Python client library supports these types within schemas:

*   `int`
*   `float`
*   `bool`
*   `str`
*   `list[AllowedType]` (where `AllowedType` is any of the allowed types)
*   `dict[str, AllowedType]` (all dictionary values must be the same type; doesn't specify keys)
*   **User-defined Pydantic Models:**  This is the most powerful option. It allows you to:
    *   Specify key names.
    *   Define different types for values associated with each key.
    *   Create nested structures.

USING ENUMS TO CONSTRAIN OUTPUT:

*   **Purpose:**  Force the model to choose *one* option from a predefined list.  This is useful for classification or multiple-choice scenarios.
*   **How it Works:** You pass an enum class (a list of strings) in the `response_schema`.
*   **Example (Illustrative):**
    ```python
    class Instrument(enum.Enum):
      PERCUSSION = "Percussion"
      STRING = "String"
      ...
    config={'response_mime_type': 'text/x.enum', 'response_schema': Instrument}
    ```
    This sets the output type to `text/x.enum` and uses the `Instrument` enum to limit responses.
* **Enum as JSON:**
    ```
      'response_schema': {
          "type": "STRING",
          "enum": ["Percussion", "String", "Woodwind", "Brass", "Keyboard"],
       }
    ```
*   **Flexibility:** Enums can be used *anywhere* a `str` would be valid within a JSON schema or for function calling.

KEY TAKEAWAYS:

*   For structured output, use `response_schema` in the model configuration for best results.
*   Pydantic models offer the most control over the JSON structure.
*   Enums are powerful for limiting the model's output to specific choices.
*   Understanding the schema definition syntax is crucial for effective use.
* The supported models are Gemini 1.5 Flash and Gemini 1.5 Pro.

--------------------------------------------------------------------------------