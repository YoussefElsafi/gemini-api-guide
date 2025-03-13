--------------------------------------------------------------------------------
       Gemini API: Safety Guidance and Settings (Detailed Guide)
--------------------------------------------------------------------------------

OVERVIEW:

This document outlines the safety considerations when building applications with Large Language Models (LLMs) through the Gemini API, including potential risks, mitigation strategies, testing approaches, and adjustable safety settings. LLMs are powerful but can produce unexpected outputs (inaccurate, biased, offensive), so responsible development is crucial.

I. GENERAL SAFETY GUIDANCE:

A. Safety Risks:

1.  Unexpected Outputs: LLMs can generate text that is offensive, insensitive, factually incorrect, or biased.

2.  Versatility Challenges: The versatility of LLMs makes it difficult to predict all potential undesirable outputs.

3.  Generative AI Prohibited Use Policy:  Your use of the Gemini API is subject to Google's Generative AI Prohibited Use Policy and the Gemini API Terms of Service.

B. Recommended Steps for Building Safe Applications:

1.  Understand the Safety Risks of Your Application.

2.  Consider Adjustments to Mitigate Safety Risks.

3.  Perform Safety Testing Appropriate to Your Use Case.

4.  Solicit Feedback from Users and Monitor Usage.

C. Understanding Safety Risks:

1.  User Awareness: Identify potential harms your application may cause to its users. This requires understanding your users and the potential impacts.

2.  Risk Assessment: Consider the likelihood of harm and its seriousness. Some applications will need to be more careful than others.

3.  Research: Research your end users, state-of-the-art studies in your app domain, observe similar apps, conduct user studies/surveys/interviews.

D. Adjustments to Mitigate Safety Risks:

1.  Tuning the Model: Fine-tuning can make the model output more predictable and consistent, helping mitigate certain risks.

2.  Input Methods: Providing safer input methods through UX design. Restrict users to choose only from a drop-down list of input prompts, or offer pop-up suggestions with descriptive phrases which you've found perform safely in your application context.

3.  Blocking and Filtering:

    *   Use blocklists to identify and block unsafe words or phrases in prompts or responses.
    *   Human reviewers can manually alter or block such content. *Warning:* Static list can be unsafe to use because it can target a particular group.
    *   Train Classifiers: Use trained classifiers to label each prompt with potential harms or adversarial signals. Block or alter the request based on the detected harm.

4.  Safeguards Against Misuse:

    *   Assign each user a unique ID.
    *   Impose limits on the volume of user queries.
    *   Protect against prompt injection.

5.  Adjusting Functionality:

    *   Narrower scope tasks (keyword extraction) or human oversight (reviewing short-form content) often pose lower risks.
    *   Instead of creating an application to write an email reply from scratch, you might instead limit it to expanding on an outline or suggesting alternative phrasings.

E. Performing Safety Testing:

1.  Varying Testing Extent:  Testing is a key part of building robust and safe applications.

2.  Safety Benchmarking:

    *   Design safety metrics that reflect the ways your application could be unsafe.
    *   Test how well your application performs on the metrics using evaluation datasets.
        *   Evaluation Metrics.
        *   Performance on the Safety Metrics.

3.  Adversarial Testing:

    *   Proactively try to break your application to identify points of weakness.
    *   Requires significant time/effort from evaluators with expertise.
        *   Identify possible weaknesses that could occur.
        *    Systematically evaluate an ML model to see how it behaves when given unwanted input.
        *   Select test data that is likely to elicit unwanted behavior from the model.
        *   Consult Google's responsible AI practices for building a test dataset.

4.  Different Outputs: Because LLMs often produce different outputs for the same prompt. Testing must be done in multiple rounds.

F. Monitoring for Problems:

1.  Feedback Channels: Set up monitored channels for users to share feedback (e.g., thumbs up/down ratings).

2.  User Studies: Run user studies to proactively solicit feedback from a diverse mix of users, especially if usage patterns are different from expectations.

II. SAFETY SETTINGS IN GEMINI API:

A. Adjustable Safety Filters:

1.  Categories:
    *   Harassment: Negative or harmful comments targeting identity and/or protected attributes.
    *   Hate speech: Content that is rude, disrespectful, or profane.
    *   Sexually explicit: Contains references to sexual acts or other lewd content.
    *   Dangerous: Promotes, facilitates, or encourages harmful acts.
    *   Civic integrity: Election-related queries.
    *   These categories are defined in HarmCategory. The Gemini models only support HARM_CATEGORY_HARASSMENT, HARM_CATEGORY_HATE_SPEECH, HARM_CATEGORY_SEXUALLY_EXPLICIT, HARM_CATEGORY_DANGEROUS_CONTENT, and HARM_CATEGORY_CIVIC_INTEGRITY. All other categories are used only by PaLM 2 (Legacy) models.

2.  Built-in Protections:  The Gemini API has built-in protections against core harms, such as content that endangers child safety. *These harms are always blocked and cannot be adjusted.*

B. Content Safety Filtering Level:

1.  Probability Levels: The Gemini API categorizes the probability level of content being unsafe as HIGH, MEDIUM, LOW, or NEGLIGIBLE.

2.  Probability vs. Severity: The Gemini API blocks content based on the *probability* of content being unsafe, *not* the severity.

3.  Importance of Testing: Test what the right block level is to support your key use cases.

C. Safety Filtering Per Request:

1.  Safety Rating: When you make a request, the content is analyzed and assigned a safety rating (category and probability).

2.  Default Blocking: By default, content (including prompts) with a medium or higher probability of being unsafe is blocked across all filters. This is designed for most use cases.

3.  Adjustable Thresholds: You can adjust the blocking thresholds for each category using the following options:

    | Threshold (Google AI Studio) | Threshold (API)               | Description                                                                                                                                         |
    | ---------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Block none                   | BLOCK_NONE                    | Always show regardless of probability of unsafe content                                                                                             |
    | Block few                    | BLOCK_ONLY_HIGH               | Block when high probability of unsafe content                                                                                                       |
    | Block some                   | BLOCK_MEDIUM_AND_ABOVE        | Block when medium or high probability of unsafe content                                                                                             |
    | Block most                   | BLOCK_LOW_AND_ABOVE           | Block when low, medium, or high probability of unsafe content                                                                                        |
    | N/A                          | HARM_BLOCK_THRESHOLD_UNSPECIFIED | Threshold is unspecified, block using default threshold                                                                                             |
    The default block threshold for the Civic integrity category is Block none (for gemini-2.0-flash-001 aliased as gemini-2.0-flash, gemini-2.0-pro-exp-02-05, and gemini-2.0-flash-lite-02-05) both for Google AI Studio and the Gemini API, and Block most for all other models in Google AI Studio only.
D. Safety Feedback:

1.  GenerateContentResponse: The generateContent method returns a GenerateContentResponse which includes safety feedback.

2.  Prompt Feedback: Prompt feedback is included in promptFeedback. If promptFeedback.blockReason is set, then the content of the prompt was blocked.

3.  Candidate Feedback: Response candidate feedback is included in Candidate.finishReason and Candidate.safetyRatings. If the response was blocked, the finishReason will be SAFETY, and you can inspect safetyRatings for details. The blocked content is not returned.

E. Adjusting Safety Settings:

1.  Google AI Studio:

    *   Click Edit safety settings in the Run settings panel to open the Run safety settings modal.
    *   Use the sliders to adjust the content filtering level per safety category.
    *   Google AI Studio will display a reminder about the Gemini API's Terms of Service with respect to safety settings if filters are set to Block none.

2.  Gemini API SDKs:

    *   Use the safetySettings parameter in the GenerateContent call to adjust thresholds.

    Python Example:

    ```python
    from google import genai
    from google.genai import types

    client = genai.Client(api_key="GEMINI_API_KEY")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Tell me something offensive.",
        config=types.GenerateContentConfig(
          safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
          ]
        )
    )

    print(response.text)
    ```

    *   This code sets the thresholds for hate speech and harassment categories.
    *   Setting these categories to BLOCK_LOW_AND_ABOVE blocks any content that has a low or higher probability of being hate speech or harassment.

III. NEXT STEPS:

*   Review the API reference.
*   Review the Safety Guidance.
*   Learn more about assessing probability versus severity from the Jigsaw team.
*   Learn more about safety solutions like the Perspective API.