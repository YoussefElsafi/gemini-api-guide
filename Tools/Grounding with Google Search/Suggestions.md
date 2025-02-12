--------------------------------------------------------------------------------
    Gemini API: Displaying Google Search Suggestions (Implementation Details)
--------------------------------------------------------------------------------

This document outlines the specific implementation requirements for displaying Google Search Suggestions when using the Gemini API's "Grounding with Google Search" feature. Adhering to these requirements is *mandatory*.

CORE PRINCIPLE:  Display Google Search Suggestions prominently and ensure they link directly to the Google Search results page (SRP) for the suggested query.

DATA SOURCE:

The `webSearchQueries` field within the `groundingMetadata` of a grounded response contains the exact search queries you must display as suggestions.

LOCATION:

The `searchEntryPoint.renderedContent` field within the `groundingMetadata` of a grounded response contains HTML and CSS styling already compliant for rendering search suggestions in your application.

DISPLAY REQUIREMENTS:

*   **Exact Match:** Display the Search Suggestion *exactly as provided* in the `webSearchQueries` field, without any modifications.  This includes spelling, capitalization, and punctuation.
*   **No Modifications:** Do not make any changes to colors, fonts, appearance, or styling of the search suggestion as provided in the HTML and CSS code. You must use the code provided in the `searchEntryPoint.renderedContent`.
*   **Visual Consistency:** Ensure the Search Suggestion renders correctly in both light and dark modes. The provided HTML and CSS (using `@media(prefers-color-scheme)`) automatically handle this.
*   **Visibility:** Whenever a grounded response is shown, its corresponding Google Search Suggestion(s) *must remain visible*.
*   **Width:** Google Search Suggestions should be at minimum the full width of the grounded response.

PROHIBITIONS ("DON'TS"):

*   **No Interstitial Screens:** Do *not* include any interstitial screens, confirmation dialogs, or additional steps between the user's tap and the display of the SRP.
*   **No Additional Suggestions/Results:** Do *not* display any other search results or suggestions alongside the Search Suggestion or the associated grounded LLM response.  The grounded response and suggestion must be presented in isolation.

BEHAVIOR ON TAP (CLICK/TOUCH):

*   **Direct Link to SRP:** When a user taps (clicks or touches) the Search Suggestion, they must be taken *directly* to the Google Search results page (SRP) for the search term displayed in the suggestion.
*   **Unobstructed SRP:** Do *not* minimize, remove, or obstruct the SRP's display in any way. The SRP must be fully visible.
*   **Browser Choice:** The SRP can open either within your in-app browser or in a separate browser app (the user's default browser).

CODE IMPLEMENTATION:

Use the compliant HTML and CSS styling provided in the `renderedContent` field of the API response to display the Search Suggestions in your application.

```html
<!--  Example:  Replace this with the actual content from renderedContent -->
<div class="container">
  <a class="chip" href="[Link to Google Search Results]"> [Search Suggestion Text] </a>
</div>
```

Important:

*   The provided HTML and CSS automatically adapt to the user's device settings, displaying in either light or dark mode based on the user's preference (indicated by `@media(prefers-color-scheme)`).

BRANDING:

You must strictly follow Google's Guidelines for Third Party Use of Google Brand Features.