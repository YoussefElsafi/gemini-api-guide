--------------------------------------------------------------------------------

                     Imagen Prompt Guide (for Gemini API)

--------------------------------------------------------------------------------

INTRODUCTION:

This guide explains how to write effective prompts for Imagen (specifically Imagen 3 accessed through the Gemini API), Google's text-to-image model.  A prompt is a text description of the image you want Imagen to generate.  The quality of your prompt significantly impacts the quality of the generated image.

PROMPT WRITING BASICS:

*   **Maximum Prompt Length:** 480 tokens.
*   **Core Elements:**  A good prompt typically includes:
    *   **Subject:** The main object, person, animal, or scene you want in the image (e.g., "a cat," "a mountain range," "an old car").
    *   **Context/Background:**  Where the subject is located or what surrounds it (e.g., "in a sunny garden," "on a deserted beach," "against a futuristic cityscape").
    *   **Style:** The artistic style or visual appearance (e.g., "photorealistic," "oil painting," "watercolor," "sketch," "3D render").

*   **Iteration is Key:**  Start with a basic prompt and then iteratively refine it by adding details, changing wording, and experimenting until you get the desired result.

IMAGEN 3 PROMPT WRITING (Specific Advice):

*   **Short vs. Long Prompts:**
    *   **Short Prompts:**  Good for quick image generation when you don't need extreme detail.
    *   **Long Prompts:** Allow you to add specific details and build a more complex image.  Imagen 3 handles both well.
*   **Descriptive Language:** Use vivid adjectives and adverbs to create a clear picture for the model (e.g., "a *fluffy*, *white* cat," "a *towering*, *snow-capped* mountain").
*   **Context is Important:**  Provide background information to help the model understand the scene.
*   **Referencing Styles/Artists:**  If you want a specific aesthetic, mention art movements (e.g., "Impressionism," "Cubism") or specific artists (e.g., "in the style of Van Gogh").
* **Prompt engineering tools:** Use resources to refine the prompts.
* **Enhancing facial details:** Use keywords like "portrait".

GENERATING TEXT IN IMAGES (Imagen 3):

*   **Improved Text Rendering:** Imagen 3 is significantly better at incorporating text into images than previous models.
*   **Best Practices:**
    *   **Keep it Short:**  Limit text to 25 characters or less for the best results.
    *   **Multiple Phrases:**  Experiment with 2-3 short phrases for more complex text. Avoid exceeding three phrases.
    *   **Guide Placement:**  You can suggest where the text should be placed, but expect some variation. This feature is still improving.
    *   **Inspire Font Style:**  Specify a general font style (e.g., "bold," "italic," "handwritten") to influence the model's choice.  Don't expect exact font replication.
    *  **Font Size:** Specify or indicate (small, medium, large) the font size.

*   **Iteration:**  You may need to generate multiple images to get the text exactly as you want it.

PROMPT PARAMETERIZATION:

*   **Concept:**  Create prompts with placeholders that can be filled in with different values.  This is useful for creating templates or allowing users to customize images.
*   **Example:**
    ```
    "A {logo_style} logo for a {company_area} company on a solid color background.  Include the text {company_name}."
    ```
    *   `{logo_style}`, `{company_area}`, and `{company_name}` are parameters that can be replaced with specific values.

ADVANCED PROMPT WRITING TECHNIQUES:

*   **Photography Modifiers:**  Control photographic aspects:
    *   **Camera Proximity:**  "close-up," "zoomed out," "taken from far away"
    *   **Camera Position:** "aerial," "from below," "eye-level"
    *   **Lighting:** "natural lighting," "dramatic lighting," "warm lighting," "cold lighting"
    *   **Camera Settings:** "motion blur," "soft focus," "bokeh," "portrait mode"
    *   **Lens Types:** "35mm lens," "50mm lens," "fisheye lens," "wide-angle lens," "macro lens"
    *   **Film Types:**  "black and white film," "polaroid"

*   **Shapes and Materials:**  Create unusual combinations:
    *   "...made of [material]" (e.g., "a chair made of clouds")
    *   "...in the shape of [object]" (e.g., "a cloud in the shape of a dragon")

*   **Historical Art References:**
    *   "...in the style of [art period/movement]" (e.g., "in the style of Art Deco," "in the style of a Renaissance painting")

*   **Image Quality Modifiers:**  Improve overall image quality:
    *   **General:** "high-quality," "beautiful," "stylized"
    *   **Photos:** "4K," "HDR," "studio photo"
    *   **Art/Illustration:** "by a professional," "detailed"

ASPECT RATIOS (Imagen 3):

*   Imagen 3 supports generating images in different aspect ratios:
    *   **1:1 (Square - Default):**  Good for social media.
    *   **4:3 (Fullscreen):**  Common for media/film, older TVs.
    *   **3:4 (Portrait Fullscreen):**  Rotated 4:3, good for vertical subjects.
    *   **16:9 (Widescreen):**  Standard for modern TVs, monitors, landscape photos.
    *   **9:16 (Portrait Widescreen):**  Rotated 16:9, good for tall, vertical subjects.
* You can combine aspect ratio in the prompt.

PHOTOREALISTIC IMAGES:
* There are keywords that can help to get photorealistic images.
* Table with suggestions.

EXAMPLES:

The document provides numerous example prompts and corresponding images to illustrate the different techniques:

*   Basic prompts (subject, context, style)
*   Short vs. long prompts
*   Text generation
*   Photography modifiers
*   Shapes and materials
*   Historical art styles
*   Image quality modifiers
*   Aspect ratios
* Tables for photorealistic images.

KEY TAKEAWAYS:

*   Start with a clear subject, context, and style.
*   Use descriptive language.
*   Iterate and refine your prompts.
*   Experiment with photography modifiers, shapes, materials, and art styles.
*   Use the aspect ratio parameter to control image dimensions.
*   Leverage Imagen 3's improved text rendering capabilities.
* Use the prompt parameterization technique to have a more generic prompts.
* Use photorealistic keywords to get such results.

This `guide.md` provides a comprehensive, practical guide to writing effective prompts for Imagen 3 within the Gemini API. It covers basic principles, advanced techniques, and specific features like text generation and aspect ratio control, with numerous examples to illustrate the concepts. It's a valuable resource for anyone wanting to get the most out of this powerful text-to-image model.