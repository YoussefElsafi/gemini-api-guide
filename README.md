# New Google GenAI Gemini SDK API Guide

This repository showcases the capabilities of the Gemini AI models using the latest Google Gemini SDK (v1.2.0). It's designed to be an accessible resource for both beginners and experienced developers looking to leverage the power of AI in their projects.

**⚠️ Warning: Important Version Requirement** ⚠️

This repository is only works with Google `google-genai` Python library v1.2.0 or higher.  It **will not function correctly** with an older version of the library.  Please ensure you have the correct version installed:

```bash
pip install -U google-genai==1.2.0
```

## Table of Contents

1.  [Overview](#overview)
2.  [Repository Structure](#repository-structure)
3.  [Getting Started](#getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation)
    *   [API Key Setup](#api-key-setup)
4.  [Code Examples](#code-examples)
    *   [AI Audio Understanding](#ai-audio-understanding)
    *   [AI Document Understanding](#ai-document-understanding)
    *   [AI Text Generation](#ai-text-generation)
    *   [AI Vision Analysis](#ai-vision-analysis)
    *   [Creative Ideas - Analyze Zip Files](#creative-ideas---analyze-zip-files)
    *   [Fine-Tuning](#fine-tuning)
    *   [Gemini 2.0 - Multimodal Live API](#gemini-20---multimodal-live-api)
    *   [Gemini 2.0 - Thinking](#gemini-20---thinking)
    *   [Image Generation - Gemini 2.0 Native Image Output](#image-generation---gemini-20-native-image-output)
    *   [Image Generation (Imagen)](#image-generation-imagen)
    *   [Safety Settings](#safety-settings)
    *   [Tools - Code Execution](#tools---code-execution)
    *   [Tools - Function Calling (Advanced)](#tools---function-calling-advanced)
    *   [Tools - Grounding with Google Search](#tools---grounding-with-google-search)
    *   [Tools - Structured Output](#tools---structured-output)
5.  [Contributing](#contributing)
6.  [License](#license)

## Overview

This repository provides a collection of Python scripts that demonstrate various AI tasks using the Gemini models.  The examples are organized into logical categories, such as:

*   **Audio Understanding:** Analyze and transcribe audio.
*   **Document Understanding:** Extract information from PDFs and other document formats.
*   **Text Generation:**  Generate creative text formats.
*   **Vision Analysis:**  Understand images and videos.
*   **Tools:**  Use specialized functionalities like code execution, function calling, and Google Search integration.
*   **Fine-Tuning:** Customize Gemini models for specific tasks.
* **Image Generation:** Generate images using text prompts, including Gemini 2.0's native image output capabilities.

Each example includes a brief description of its purpose and instructions for running it. This repository is aimed at providing code examples for each category, enabling users to build AI powered applications.

## Repository Structure

The repository is structured as follows:

```
gemini-api-guide/
  + AI Audio Understanding/
    - Advanced_Music_Analysis.py
    + Audios/
      - Long_Speech.wav
      - Sample.mp3
      - Speech.wav
    - Details.md
    - Music_Analysis.py
    - Timestamp.py
    - Transcript_Speech.py
  + AI Document Understanding/
    - Access_document_from_url.py
    - Details.md
    - Document_Analysis.py
    + Documents/
      - PDF.pdf
    - Download_URL_Document_and_analyze.py
    - Upload_And_Download_URL_Document_and_analyze.py
    - Upload_Documents.py
  + AI Text Generation/
    - Details.md
    - system_instructions.py
    - text_gen.py
    - text_gen_chat.py
    - text_gen_chat_stream.py
    - text_gen_config.py
    - text_input_stream.py
  + AI Vision Analysis/
    + Image Input/
      - Base64_encoded_image.py
      - Details.md
      + Images/
        - Example_Image.png
        - Example_Image2.jpg
      - Local_Image.py
      - Multiple_Images.py
      - Upload_images.py
    + Spatial Understanding/
      - ObjectBounding.py
      + images/
        - Example_Image.png
    + Video Input/
      - Details.md
      - Summarize_Video.py
      - Transcribe_Video_Audio.py
      - Verify_Uploaded_Video.py
      - Video_TimeStamp_Analysis.py
      + Videos/
        - Example_Video.mp4
        - GreatRedSpot.mp4
      - list_Uploaded_videos.py
  + Creative Ideas/
    + Analyze Zip Files/
      - main.py
  + Fine-Tuning/
    - Create_Tuning_Model.py
    - Details.md
    - Generate_using_Tuned_Model.py
    - List_Tuned_Models.py
  + Gemini 2.0/
    + Multimodal Live API/
      - Details.md
    + Thinking/
      - Details.md
  + Image Generation/
    + Gemini 2.0 Native Image Output/
      - Details.md
      - ImageEditing.py
      - ImageGeneration.py
      - MultiImageEditing.py
      + generated_images/
      + images/
        - car.jpg
        - croissant.jpeg
    + Imagen/
      - Details.md
      - Guide.md
      - imagen.py
  + Safety Settings/
    - Details.md
    - check_blocked_content.py
    - set_safety_thresholds.py
  + System Instructions/
  + Tools/
    + Code Execution/
      - Details.md
      - code_execution.py
      - code_execution_chat.py
    + Function Calling (Advanced)/
      + Controlling Lights Example/
        - Function_Call.py
      - Details.md
      + Parallel Functions Examples/
        + automatic_function_declarations/
          + Party/
            - automatic_party_functions.py
            - parallel_functions.py
          + Weather/
            - automatic_weather_forecast.py
          + e_commerce/
            - automatic_product_search.py
        + manual_function_declarations/
          + Party/
            - manual_party_functions.py
          + Weather/
            - manual_weather_forecast.py
          + e_commerce/
            - manual_product_search.py
    + Grounding with Google Search/
      - Details.md
      + Grounding/
        - Dynamic_Grounding_Threshold.py
        - Grounding.py
      + Search as a Tool (Gemini 2.0)/
        - Search.py
      - Suggestions.md
    + structured_output/
      - Details.md
      - enum_choice_output.py
      - instrument_enum_output.py
      - instrument_enum_output_json_configuration.py
      - through_model_configuration.py
      - using_prompt.py
```

*   Each top-level directory (e.g., `AI Audio Understanding`, `AI Document Understanding`) represents a specific AI capability.
*   `Details.md` files within each directory provide in-depth explanations of the relevant concepts and API features.
*   Python (`.py`) files contain the runnable code examples.
*   Supporting directories (e.g., `Audios`, `Documents`, `Images`, `Videos`) hold the data used by the example scripts.

## Getting Started

This section guides you through setting up your environment and running the example code.

### Prerequisites

*   **Python 3.9 or higher:**  Ensure you have Python installed. You can check your version by running `python --version` in your terminal.
*   **pip:** Python package installer (should come with your Python installation).
*   **A Google Cloud project:** While not strictly required for all examples, some features might require a Google Cloud project and enabling the Gemini API.
*   **A Gemini API key:**  You'll need an API key to access the Gemini models. Get it from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YoussefElsafi/gemini-api-guide
    cd gemini-api-guide
    ```
    Replace `[repository URL]` with the actual URL of this GitHub repository.

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate.bat # On Windows
    ```
    Using a virtual environment helps isolate the project's dependencies.

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    This will install the Google Gemini AI library along with any other dependencies.
    ***NOTE:*** If the `requirements.txt` doesn't work, make sure to install `google-genai` as v1.2.0

### API Key Setup

1.  **Set the API key as an environment variable:**

    The examples in this repository assume that your Gemini API key is stored in an environment variable named `API_KEY`.

    *   **Linux/macOS:**
        ```bash
        export API_KEY="YOUR_API_KEY"
        ```
    *   **Windows:**
        ```bash
        set API_KEY="YOUR_API_KEY"
        ```
    Replace `"YOUR_API_KEY"` with your actual API key.  You can also set it permanently in your system's environment variables.

## Code Examples

Each of the following sections corresponds to a directory in the repository.  They provide a brief overview and instructions for running the examples.

### AI Audio Understanding

This directory contains examples for analyzing and transcribing audio files.

*   **`Advanced_Music_Analysis.py`:** (To be implemented)  Performs advanced analysis of music files (e.g., genre classification, tempo detection).
*   **`Music_Analysis.py`:** (To be implemented) Analyzes audio for birdsongs, sirens, and more.
*   **`Timestamp.py`:** Transcribes the speech from audio between timestamps.
*   **`Transcript_Speech.py`:** Transcribes spoken content from an audio file.
*   **`Audios/`:** Contains sample audio files (`Long_Speech.wav`, `Sample.mp3`, `Speech.wav`).
*   **Details.md:** Provides a detailed documentation of the audio processing capabilities of the Gemini API.

**To run the examples:**

1.  Navigate to the `AI Audio Understanding` directory:
    ```bash
    cd "gemini-api-guide/AI Audio Understanding"
    ```
2.  Run the desired Python script:
    ```bash
    python Transcript_Speech.py  
    ```
   Make sure to set your API key.

### AI Document Understanding

This directory showcases how to extract information from various document types.

*   **`Access_document_from_url.py`:** Summarizes a document retrieved from a URL.
*   **`Document_Analysis.py`:** (To be implemented) Performs more comprehensive document analysis (e.g., entity recognition, sentiment analysis).
*   **`Documents/`:**  Contains a sample PDF file (`PDF.pdf`).
*   **`Download_URL_Document_and_analyze.py`:** Downloads and analyzes a document from a given URL.
*   **`Upload_And_Download_URL_Document_and_analyze.py`:** Downloads a document from a URL and analyzes its content.
*   **`Upload_Documents.py`:** Analyzes the content of a document.
*   **Details.md:** Contains a detailed guide to using the Gemini API's PDF processing capabilities.

**To run the examples:**

1.  Navigate to the `AI Document Understanding` directory:
    ```bash
    cd "gemini-api-guide/AI Document Understanding"
    ```
2.  Run the desired script:
    ```bash
    python Access_document_from_url.py 
    ```
   Make sure to set your API key.

### AI Text Generation

This directory provides examples of generating text using different techniques and configurations.

*   **`text_gen.py`:** Generates text from a simple text prompt.
*   **`text_gen_chat.py`:** Creates a chat conversation with the model.
*   **`text_gen_chat_stream.py`:** Generates a streaming chat conversation.
*   **`text_gen_config.py`:** Configures text generation parameters like `max_output_tokens` and `temperature`.
*   **`text_input_stream.py`:** Generates text using a stream of text as input.
*   **`system_instructions.py`:** Uses system instructions to guide the model's behavior.
*   **Details.md:** Comprehensive guide on using the Gemini API for text generation.

**To run the examples:**

1.  Navigate to the `AI Text Generation` directory:
    ```bash
    cd "gemini-api-guide/AI Text Generation"
    ```
2.  Run the desired script:
    ```bash
    python text_gen.py  
    ```
    Make sure to set your API key.

### AI Vision Analysis

This directory contains examples demonstrating how to analyze images and videos.  It's further divided into subdirectories for different input types:

#### Image Input

*   **`Base64_encoded_image.py`:** (To be implemented) Analyzes an image provided as a Base64 encoded string.
*   **`Local_Image.py`:** Analyzes a local image file.
*   **`Multiple_Images.py`:** Analyzes multiple images to find common themes.
*   **`Upload_images.py`:** Uploads images to Gemini and gets descriptive context.
*   **`Images/`:** Contains sample image files (`Example_Image.png`, `Example_Image2.jpg`).
*   **Details.md:** Contains a detailed guide to using the Gemini API for image analysis.

**To run the examples:**

1.  Navigate to the `Image Input` directory:
    ```bash
    cd "gemini-api-guide/AI Vision Analysis/Image Input"
    ```
2.  Run the desired script:
    ```bash
    python Local_Image.py  
    ```
    Make sure to set your API key.

#### Spatial Understanding

*   **`ObjectBounding.py`:** Analyzes an image and detects the location of objects within the image.
*   **`images/`:** Contains sample image files (`Example_Image.png`).

**To run the examples:**

1.  Navigate to the `Spatial Understanding` directory:
    ```bash
    cd "gemini-api-guide/AI Vision Analysis/Spatial Understanding"
    ```
2.  Run the desired script:
    ```bash
    python ObjectBounding.py  
    ```
    Make sure to set your API key.

#### Video Input

*   **`Summarize_Video.py`:** Summarizes a video file.
*   **`Transcribe_Video_Audio.py`:** Transcribes the audio from a video.
*   **`Verify_Uploaded_Video.py`:** Uploads and verifies the upload of a video.
*   **`Video_TimeStamp_Analysis.py`:** Analyzes a video for specific events at given timestamps.
*   **`list_Uploaded_videos.py`:** (To be implemented) Lists the uploaded videos.
*   **`Videos/`:** Contains sample video files (`Example_Video.mp4`, `GreatRedSpot.mp4`).
*   **Details.md:** Outlines the video capabilities of Gemini 1.5 Pro and Flash models.

**To run the examples:**

1.  Navigate to the `Video Input` directory:
    ```bash
    cd "gemini-api-guide/AI Vision Analysis/Video Input"
    ```
2.  Run the desired script:
    ```bash
    python Summarize_Video.py  
    ```
    Make sure to set your API key.

### Creative Ideas - Analyze Zip Files

This directory contains an example demonstrating a creative use of Gemini: analyzing the contents of a ZIP file.

*   **`main.py`:**  Prompts the user for a ZIP file path, extracts its contents to a temporary directory, generates a file tree structure, identifies supported files, and then uses Gemini to analyze the contents based on a user-provided prompt.

**To run the example:**

1.  Navigate to the `Analyze Zip Files` directory:
    ```bash
    cd "gemini-api-guide/Creative Ideas/Analyze Zip Files"
    ```
2.  Run the script:
    ```bash
    python main.py
    ```
    Make sure to set your API key.

### Fine-Tuning

This directory showcases how to fine-tune Gemini models for specific tasks.

*   **`Create_Tuning_Model.py`:** Creates a new tuned model based on a training dataset.
*   **`Generate_using_Tuned_Model.py`:** Generates content using a pre-tuned model.
*   **`List_Tuned_Models.py`:** Lists the available tuned models.
*   **Details.md:** Provides a conceptual overview and practical tutorial on using Gemini API for fine-tuning.

**To run the examples:**

1.  Navigate to the `Fine-Tuning` directory:
    ```bash
    cd "gemini-api-guide/Fine-Tuning"
    ```
2.  Run the desired script:
    ```bash
    python Create_Tuning_Model.py  
    ```
    Make sure to set your API key.

### Gemini 2.0 - Multimodal Live API

*   **`Details.md`:** A comprehensive summary of the Multimodal Live API, covering its capabilities, how to use it, integration details, limitations, and a breakdown of the message types.

### Gemini 2.0 - Thinking

*   **`Details.md`:** Explains the Gemini 2.0 Flash Thinking model, an experimental model designed to reveal its "thinking process" during response generation.

### Image Generation - Gemini 2.0 Native Image Output

This section demonstrates the native image generation capabilities of Gemini 2.0.  Unlike the separate Imagen model, Gemini 2.0 can directly generate images within its multimodal framework.

*   **`ImageGeneration.py`:** Generates an image from a text prompt using Gemini 2.0's native image output.
*   **`ImageEditing.py`:** Edits an existing image based on text instructions, demonstrating in-context image manipulation.
*   **`MultiImageEditing.py`:**  Edits multiple images simultaneously, applying consistent changes based on a single text prompt.
*   **`images/`:** Contains input images for editing examples (`car.jpg`, `croissant.jpeg`).
*   **`generated_images/`:**  This directory will store the images generated by the scripts.
*   **`Details.md`:** Provides a comprehensive guide to using Gemini 2.0 for native image generation, covering prompting techniques, editing capabilities, and limitations.  It contrasts this native functionality with the separate Imagen model.

**To run the examples:**

1.  Navigate to the `Gemini 2.0 Native Image Output` directory:
    ```bash
    cd "gemini-api-guide/Image Generation/Gemini 2.0 Native Image Output"
    ```
2.  Run the desired script:
    ```bash
    python ImageGeneration.py  
    ```
    Make sure to set your API key.

### Image Generation (Imagen)

This directory provides examples of using the Imagen model for text-to-image generation.

*   **`imagen.py`:** Generates an image from a text prompt.
*   **`Guide.md`:** A comprehensive, practical guide to writing effective prompts for Imagen 3.
*   **`Details.md`:** Text-to-image generation.

**To run the examples:**

1.  Navigate to the `Image Generation (Imagen)` directory:
    ```bash
    cd "gemini-api-guide/Image Generation (Imagen)"
    ```
2.  Run the script:
    ```bash
    python imagen.py  
    ```
    Make sure to set your API key.
### Safety Settings

This directory demonstrates how to adjust the safety settings of the Gemini API.

*   **`check_blocked_content.py`:** Checks and filters blocked content in the prompt.
*   **`set_safety_thresholds.py`:** Sets the safety thresholds for different content categories.
*   **Details.md:**  Outlines the safety considerations when building applications with Large Language Models (LLMs) through the Gemini API.

**To run the examples:**

1.  Navigate to the `Safety Settings` directory:
    ```bash
    cd "gemini-api-guide/Safety Settings"
    ```
2.  Run the desired script:
    ```bash
    python set_safety_thresholds.py  
    ```
    Make sure to set your API key.

### Tools - Code Execution

This directory provides examples of using the code execution tool.

*   **`code_execution.py`:** Generates and executes Python code to perform calculations.
*   **`code_execution_chat.py`:** Creates a chat interface that can execute code.
*   **Details.md:** Explains the Gemini API's code execution feature empowers the model to generate and run Python code.

**To run the examples:**

1.  Navigate to the `Code Execution` directory:
    ```bash
    cd "gemini-api-guide/Tools/Code Execution"
    ```
2.  Run the desired script:
    ```bash
    python code_execution.py  
    ```
    Make sure to set your API key.

### Tools - Function Calling (Advanced)

This directory showcases the advanced function calling capabilities of Gemini.

*   **`Function_Call.py`:** Demonstrates a basic example of function calling, controlling lights.
*   **`automatic_function_declarations/`:** Use function annotations for automatic function declarations.
    *   **`Party/`:** Turns on the spinning disco ball, plays some music, and dims the lights.
    *   **`Weather/`:** Gets the current weather for a given city, includes an illustrative example for use.
    *   **`e_commerce/`:** Searches for products in a given category, includes an illustrative example for use.
*   **`manual_function_declarations/`:** Define function declarations in `tools` for the model.
    *   **`Party/`:** Turns on the spinning disco ball, plays some music, and dims the lights.
    *   **`Weather/`:** Gets the current weather for a given city, includes an illustrative example for use.
    *   **`e_commerce/`:** Searches for products in a given category, includes an illustrative example for use.
*   **Details.md:** Explains how function calling allows Gemini models to interact with *external systems and APIs*.

**To run the examples:**

1.  Navigate to the `Function Calling (Advanced)` directory:
    ```bash
    cd "gemini-api-guide/Tools/Function Calling (Advanced)"
    ```
2.  Run the desired script:
    ```bash
    python Function_Call.py  
    ```
    Make sure to set your API key.

### Tools - Grounding with Google Search

This directory demonstrates how to use the "Grounding with Google Search" feature.

*   **`Dynamic_Grounding_Threshold.py`:** (To be implemented) Set the dynamic retrieval threshold.
*   **`Grounding.py`:** Enhances the accuracy and reliability of Gemini API responses.
*   **`Search.py`:** Enables Google Search as a tool the model can invoke itself for.
*   **`Suggestions.md`:** The `webSearchQueries` field within the `groundingMetadata`.
*   **Details.md:** Describes how to use the "Grounding with Google Search" feature within the Gemini API to enhance the accuracy, recency, and reliability of model responses.

**To run the examples:**

1.  Navigate to the `Grounding with Google Search` directory:
    ```bash
    cd "gemini-api-guide/Tools/Grounding with Google Search"
    ```
2.  Run the desired script:
    ```bash
    python Grounding.py  
    ```
    Make sure to set your API key.

### Tools - Structured Output

This directory demonstrates how to generate structured data, like JSON, for easier processing.

*   **`enum_choice_output.py`:** Use enums to constrain output.
*   **`instrument_enum_output.py`:** Enums with an instrument.
*   **`instrument_enum_output_json_configuration.py`:** In JSON format with enum.
*   **`through_model_configuration.py`:** Model Configurations.
*   **`using_prompt.py`:** Generating structured data through prompts.
*   **Details.md:** Explains generating structured output (JSON & Enums).

**To run the examples:**

1.  Navigate to the `structured_output` directory:
    ```bash
    cd "gemini-api-guide/Tools/structured_output"
    ```
2.  Run the desired script:
    ```bash
    python enum_choice_output.py  
    ```
    Make sure to set your API key.

## Contributing

We welcome contributions to this repository!  If you have a bug fix, new feature, or improved example, please submit a pull request.

## License

This repository is licensed under the [MIT License](LICENSE).
