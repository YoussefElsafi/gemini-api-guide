--------------------------------------------------------------------------------
       Gemini API: Grounding with Google Search (Detailed Guide)
--------------------------------------------------------------------------------

OVERVIEW:

This document describes how to use the "Grounding with Google Search" feature within the Gemini API to enhance the accuracy, recency, and reliability of model responses. Grounding connects the model to verifiable information sources on the internet, mitigating hallucinations and improving the trustworthiness of generated content.

KEY FEATURES:

*   Enhanced Accuracy and Recency:  Retrieves up-to-date information beyond the model's pre-existing knowledge cutoff.
*   Reduced Hallucinations:  Decreases the generation of factually incorrect or fabricated content.
*   Source Attribution: Provides inline links ("grounding sources") to the web pages used to generate the response, allowing users to verify information.
*   Google Search Suggestions: Includes suggested search queries in the response metadata, enabling users to explore related information.
*   Dynamic Retrieval:  Offers control over when Grounding with Google Search is used based on a configurable threshold.
*   Search as a Tool:  Allows the model to decide when to use Google Search, enabling more complex multi-turn conversations and workflows.

GETTING STARTED:

1.  Configuration:  To enable Grounding with Google Search, include the `google_search` tool in your API request.

    ```python
    from google import genai
    from google.genai import types

    client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

    response = client.models.generate_content(
        model='gemini-2.0-flash',  # or a suitable model supporting grounding
        contents="Who won Wimbledon this year?",
        config=types.GenerateContentConfig(
            tools=[types.Tool(
                google_search=types.GoogleSearchRetrieval
            )]
        )
    )
    print(response)
    ```

2.  Dynamic Threshold:  Control the retrieval behavior based on the prompt's need for up-to-date information. The `dynamic_threshold` setting determines when grounding is triggered.

    ```python
    from google import genai
    from google.genai import types

    client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents="Who won Wimbledon this year?",
        config=types.GenerateContentConfig(
            tools=[types.Tool(
                google_search=types.GoogleSearchRetrieval(
                    dynamic_retrieval_config=types.DynamicRetrievalConfig(
                        dynamic_threshold=0.6))  # Adjust the threshold
            )]
        )
    )
    print(response)
    ```

    *   `dynamic_threshold`:  A floating-point value between 0 and 1 (defaults to 0.3).
        *   0: Always use Grounding with Google Search.
        *   1: Never use Grounding with Google Search.
        *   Values in between:  Grounding is used based on a prediction score (see below).

3.  Languages and Pricing: Grounding with Google Search works with all available languages for text prompts. The paid tier of the Gemini Developer API provides 1,500 free queries per day, with additional queries billed at the standard rate. (Check the pricing page for current details.)

WHY USE GROUNDING WITH GOOGLE SEARCH?

*   Connects the model to verifiable information sources.
*   Improves accuracy, reliability, and usefulness of AI outputs.
*   Essential for prompts requiring up-to-date information from the web.
*   Enables responses that are tethered to specific content and provide source citations.

DYNAMIC RETRIEVAL (DETAILED):

1.  How it Works:  Dynamic retrieval allows you to control *when* Grounding with Google Search is used, optimizing for latency, quality, and cost.

2.  Terminology:

    *   **Prediction Score:**  Gemini assigns a prediction score (0 to 1) to each prompt, indicating how much the prompt would benefit from grounding. High scores suggest that the model needs grounding.
    *   **Threshold:**  The `dynamic_threshold` you configure in the API request.  A lower threshold results in more prompts being grounded.

3.  Decision Process:

    *   If the prediction score is greater than or equal to the threshold, the answer is grounded with Google Search.
    *   If the prediction score is less than the threshold, the model may still answer, but the response will *not* be grounded.

4.  Example Prediction Scores:

    | Prompt                                                     | Prediction Score | Comment                                                                        |
    | ---------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------ |
    | "Write a poem about peonies"                               | 0.13             | Model can rely on its knowledge; grounding not needed.                       |
    | "Suggest a toy for a 2yo child"                           | 0.36             | Model can rely on its knowledge; grounding not needed.                       |
    | "Recipe for an asian-inspired guacamole?"                 | 0.55             | Grounding can help, but model knowledge might suffice.                       |
    | "What's Agent Builder? How is grounding billed in it?" | 0.72             | Requires Google Search for a well-grounded answer.                             |
    | "Who won the latest F1 grand prix?"                       | 0.97             | Requires Google Search for a well-grounded answer.                             |

5.  Setting the Threshold:  You can set the dynamic retrieval threshold in the API request using the code examples provided above. In AI Studio, you can set the threshold by clicking "Edit grounding."

6.  Finding the Right Threshold:  Create a representative set of queries for your use case. Sort the queries by their prediction scores to determine a suitable threshold for your application.

SEARCH AS A TOOL:

1.  Enables the Model to Decide:  Starting with Gemini 2.0, Google Search is available as a tool that the model can invoke itself.

    ```python
    from google import genai
    from google.genai.types import Tool, GenerateContentConfig, GoogleSearch

    client = genai.Client()
    model_id = "gemini-2.0-flash"

    google_search_tool = Tool(
        google_search = GoogleSearch()
    )

    response = client.models.generate_content(
        model=model_id,
        contents="When is the next total solar eclipse in the United States?",
        config=GenerateContentConfig(
            tools=[google_search_tool],
            response_modalities=["TEXT"],
        )
    )

    for each in response.candidates[0].content.parts:
        print(each.text)

    print(response.candidates[0].grounding_metadata.search_entry_point.rendered_content) # Get grounding metadata.
    ```

2.  Complex Workflows:  Enables multi-turn searches and multi-tool queries (e.g., combining Grounding with Google Search and code execution).

3.  Applications:

    *   Enhancing factuality and recency of responses.
    *   Retrieving artifacts from the web for further analysis.
    *   Finding relevant media for multimodal reasoning.
    *   Coding, technical troubleshooting, and specialized tasks.
    *   Finding region-specific information or translating content.
    *   Finding relevant websites for further browsing.

GROUNDED RESPONSE FORMAT:

A successfully grounded response includes a `groundingMetadata` field in the API response.  Key elements include:

*   `searchEntryPoint`: Contains HTML code snippets  for displaying Google Search Suggestions. *Important:  You are required to display these suggestions.*
*   `groundingChunks`:  A list of web resources (URIs and titles) used for grounding the response.
*   `groundingSupports`: Segments of the response text linked to specific `groundingChunks`, along with confidence scores.
*   `webSearchQueries`:  The search queries used to retrieve the grounding information.

Important Considerations:

* The URIs remain accessible for 30 days after the grounded result is generated.
*  The provided URIs must be directly accessible by the end users and must not be queried programmatically through automated means.

EXAMPLE GROUNDED RESPONSE SNIPPET (ABBREVIATED):

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Carlos Alcaraz won the Gentlemen's Singles title at the 2024 Wimbledon Championships. He defeated Novak Djokovic in the final..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML code for Google Search Suggestions -->"
        },
        "groundingChunks": [
          {
            "web": {
              "uri": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/...",
              "title": "wikipedia.org"
            }
          },
          // ... more grounding chunks ...
        ],
        "groundingSupports": [
          {
            "segment": {
              "endIndex": 85,
              "text": "Carlos Alcaraz won the Gentlemen's Singles title at the 2024 Wimbledon Championships."
            },
            "groundingChunkIndices": [
              0,
              1,
              2,
              3
            ],
            "confidenceScores": [
              0.97380733,
              0.97380733,
              0.97380733,
              0.97380733
            ]
          },
          // ... more grounding supports ...
        ],
        "webSearchQueries": [
          "who won wimbledon 2024"
        ]
      }
    }
  ]
}
```

TROUBLESHOOTING:

If `groundingMetadata` is missing, the response was not successfully grounded. This can be due to low source relevance or incomplete information in the model response.

GOOGLE SEARCH SUGGESTIONS:

You **must** display Google Search Suggestions when using Grounding with Google Search.  The `searchEntryPoint.renderedContent` field provides the HTML code to implement these suggestions.

KEY TAKEAWAYS:

*   Grounding with Google Search enhances the accuracy and reliability of Gemini API responses.
*   Use the `google_search` tool in your API requests to enable grounding.
*   Configure the `dynamic_threshold` to control when grounding is used.
*   Display Google Search Suggestions (using the `searchEntryPoint` data).
*   The `groundingMetadata` field provides links to the web sources used to generate the response.
* Leverage search as a tool for more complex prompts and workflows.