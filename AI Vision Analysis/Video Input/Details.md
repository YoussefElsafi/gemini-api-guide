# Gemini 1.5 Pro and Flash - Video Support Details

This document outlines the video capabilities of Gemini 1.5 Pro and Flash models.

**Video Input Capabilities:**

* **Supported Models:** Gemini 1.5 Pro and Flash.
* **Maximum Duration:** Approximately one hour of video data.
* **Supported Video Formats (MIME Types):**
    * video/mp4
    * video/mpeg
    * video/mov
    * video/avi
    * video/x-flv
    * video/mpg
    * video/webm
    * video/wmv
    * video/3gpp

**Video Processing Details:**

* **Frame Extraction:** 1 frame per second (FPS).
* **Audio Extraction:** 1Kbps, single channel.
* **Timestamping:** Timestamps added every second.
* **Tokenization (Approximate per second of video):**
    * Individual Frames: 258 tokens
    * Audio: 32 tokens
    * Total: ~300 tokens (including metadata)
* **Context Window:** A 1M context window can accommodate slightly less than one hour of video.
* **Note on Sampling Rates:** Frame and audio extraction rates are subject to future changes for improved inference.
* **High-Speed Video:** Details in fast action sequences may be lost due to the 1 FPS frame sampling rate. Consider slowing down high-speed clips for better inference quality.

**Usage Recommendations:**

* **One Video per Prompt:** For optimal results, use only one video per prompt.
* **Prompt Placement:** When using a single video, place the text prompt *after* the video data.
* **File API Upload:** Upload video files using the File API service.

**File API Information:**

* **Purpose:**  Enables video file upload and processing for Gemini models.
* **Storage Capacity:** Up to 20 GB of files per project.
* **Maximum File Size:** 2 GB per file.
* **Storage Duration:** Files are stored for 48 hours.
* **Access:** Files can be accessed via your API key within the 48-hour storage period.
* **Download Restriction:** Files cannot be downloaded using any API.
* **Cost:** Available at no cost in all regions where the Gemini API is available.
* **Direct File Format Support:** The File API accepts video file formats directly.

**Time-Stamped Queries:**

* **Format:** Use `MM:SS` format to ask questions about specific time locations within the video (e.g., `01:30`).

**Example Video:**

* **NASA Film:** "Jupiter's Great Red Spot Shrinks and Grows" is used as an example.
* **Credit:** Goddard Space Flight Center (GSFC)/David Ladd (2018).
* **Public Domain:** The example video is in the public domain.
* **Privacy:** The example video does not show identifiable people.

**Important Notes:**

* These details are subject to change as the models and services evolve. Refer to the latest documentation for the most up-to-date information.
* Consider the limitations of the 1 FPS frame rate, especially for videos with fast-paced action.