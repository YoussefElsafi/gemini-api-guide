Topic: Prompting with Images

Description: This document outlines the technical details for prompting Gemini models with images. Users can upload images via the File API or inline data to generate content based on the image inputs.

--- Technical Specifications ---

Maximum Image Files: 3600 (Gemini 1.5 Pro & 1.5 Flash)

Supported Image MIME Types:
- image/png (PNG)
- image/jpeg (JPEG)
- image/webp (WEBP)
- image/heic (HEIC)
- image/heif (HEIF)

--- Token Calculation ---

Gemini Model Token Usage:

- Gemini 1.0 Pro Vision: 258 tokens per image.

- Gemini 1.5 Flash & 1.5 Pro:
    - Images with both dimensions <= 384 pixels: 258 tokens.
    - Images with one dimension > 384 pixels:
        - Image is tiled.
        - Default tile size: smallest dimension / 1.5.
        - Tile size adjusted to be between 256 and 768 pixels.
        - Each tile resized to 768x768 pixels.
        - 258 tokens per tile.

- Gemini 2.0 Flash:
    - Images with both dimensions <= 384 pixels: 258 tokens.
    - Images larger in one or both dimensions:
        - Image is cropped and scaled into 768x768 pixel tiles as needed.
        - 258 tokens per tile.

--- Best Practices ---

Image Preparation:
- Image Orientation: Rotate images to the correct orientation before uploading.
- Image Quality: Avoid blurry images for optimal performance.

Prompting Strategy:
- Prompt Placement (Single Image): Place text prompts after the image for single image inputs.