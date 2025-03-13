# Gemini API - Audio Capabilities Overview

This document outlines the audio processing capabilities of the Gemini API.

**Core Functionality:**

The Gemini API can analyze and understand audio content. It can perform the following tasks based on audio input:

* **Description:** Describe the content of an audio file.
* **Summarization:** Summarize the key information within an audio file.
* **Question Answering:** Answer questions related to the audio content.
* **Transcription:** Provide a text transcription of spoken content in the audio.
* **Segment Analysis:**  Analyze and provide information about specific segments of the audio.

**Important Note:** The Gemini API **cannot generate audio output.** Its functionality is limited to audio analysis and understanding for text-based responses.

**Supported Audio Formats (MIME Types):**

The Gemini API supports the following audio file formats:

* `audio/wav` (WAV)
* `audio/mp3` (MP3)
* `audio/aiff` (AIFF)
* `audio/aac` (AAC)
* `audio/ogg` (OGG Vorbis)
* `audio/flac` (FLAC)

**Technical Details & Limitations:**

* **Tokenization:**  Each second of audio is represented as approximately **25 tokens**.  (Example: 1 minute of audio = ~1,500 tokens).
* **Language Support:**  Primarily designed for **English-language speech** recognition.
* **Non-Speech Audio:** Can understand non-speech audio components like birdsong, sirens, etc.
* **Maximum Audio Length:**  A single prompt can process a maximum of **9.5 hours** of combined audio data. This limit applies to the total duration of all audio files included in a single request.
* **Audio Downsampling:**  Audio files are automatically downsampled to a **16 Kbps data resolution** for processing.
* **Channel Handling:**  Multi-channel audio sources are combined into a **single channel** before analysis.

**Methods for Providing Audio Input:**

You can make audio files accessible to the Gemini API through two methods:

1. **File API Upload:**
    * Use the File API to upload audio files of any size.
    * **Recommended for requests exceeding 20 MB** in total size (including files, text prompts, etc.).
    * Suitable for larger audio files.

2. **Inline Data in Prompt Request:**
    * Provide the audio file data directly within the prompt request.
    * Appropriate for smaller audio files and when the total request size is under 20 MB.

**Programming Languages:**

The Gemini API audio capabilities are accessible through the following programming languages and interfaces:

* **Python**
* **Node.js**
* **Go**
* **REST API**

**Before You Begin:**

Before using the Gemini API, ensure you have:

* Set up a Google Cloud project (if required).
* Configured and obtained your Gemini API key.
* Installed the necessary client libraries for your chosen programming language (Python, Node.js, Go).

**Disclaimer:**  These details are based on the provided information and may be subject to change as the Gemini API evolves. Refer to the official Gemini API documentation for the most up-to-date specifications and features.