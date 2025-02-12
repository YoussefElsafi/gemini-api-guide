--------------------------------------------------------------------------------

       Gemini API: Document Processing (Detailed Guide)

--------------------------------------------------------------------------------

OVERVIEW:

The Gemini API can process PDF documents directly, leveraging its native vision capabilities to understand both the text and visual elements (diagrams, charts, tables) within the PDFs. This allows for a wide range of document-related tasks.  This functionality works with Gemini 1.5 & 2.0 models. Output is text-only.

KEY CAPABILITIES:

*   **Diagram, Chart, and Table Analysis:**  The model can understand and extract information from visual data representations within the PDF.
*   **Structured Data Extraction:** Information from the PDF can be extracted into structured formats (like JSON).
*   **Question Answering:**  You can ask questions about the content of the PDF, including both text and visual elements.
*   **Summarization:** The model can generate summaries of the document's content.
*   **Transcription (with Layout Preservation):**  The document's content can be transcribed (e.g., to HTML), preserving the layout and formatting.  This is useful for downstream tasks like RAG (Retrieval-Augmented Generation) pipelines.

TECHNICAL DETAILS:

*   **Page Limit:**  Supports up to 3,600 document pages.
*   **Supported MIME Types:**
    *   `application/pdf` (PDF)
    *   `application/x-javascript`, `text/javascript` (JavaScript)
    *   `application/x-python`, `text/x-python` (Python)
    *   `text/plain` (TXT)
    *   `text/html` (HTML)
    *   `text/css` (CSS)
    *   `text/md` (Markdown)
    *   `text/csv` (CSV)
    *   `text/xml` (XML)
    *   `text/rtf` (RTF)
*   **Page Token Equivalence:** Each document page is equivalent to 258 tokens.
*   **Image Resolution Handling:**
    *   Larger pages are scaled down to 3072x3072 (preserving aspect ratio).
    *   Smaller pages are scaled up to 768x768.
    *   *No cost reduction* for smaller pages, and *no performance improvement* for higher resolution.
* **Best Results:**
    * Rotate the pages.
    * Avoid blur.
    * Put the prompt after single pages.

PDF INPUT METHODS:

1.  **Inline Data (for smaller PDFs, <20MB):**
    *   You can include the PDF data directly within the API request, encoded as base64.
    *   This is suitable for smaller PDF files.

    ```python
    from google import genai
    from google.genai import types
    import httpx  # For fetching the PDF from a URL

    client = genai.Client()

    doc_url = "YOUR_PDF_URL"
    doc_data = httpx.get(doc_url).content  # Fetch the PDF content

    prompt = "Summarize this document"
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            types.Part.from_bytes(
                data=doc_data,  # The PDF data as bytes
                mime_type='application/pdf',
            ),
            prompt  # Your text prompt
        ]
    )
    print(response.text)
    ```
     *  Locally Stored PDFs.
    ```python
    from google import genai
    from google.genai import types
    import pathlib
    import httpx

    client = genai.Client()

    doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"

    # Retrieve and encode the PDF byte
    filepath = pathlib.Path('file.pdf')
    filepath.write_bytes(httpx.get(doc_url).content)

    prompt = "Summarize this document"
    response = client.models.generate_content(
      model="gemini-1.5-flash",
      contents=[
          types.Part.from_bytes(
            data=filepath.read_bytes(),
            mime_type='application/pdf',
          ),
          prompt])
    print(response.text)
    ```

2.  **File API (for larger PDFs or any size):**

    *   The File API allows you to upload files (up to 2GB per file, 20GB total per project) to a temporary storage area.
    *   Files are stored for 48 hours and can be accessed using your API key (but not downloaded).
    *   *Always use the File API* if the total request size (including files, prompt, etc.) exceeds 20MB.
    *   This is the recommended approach for larger PDFs.

    ```python
    from google import genai
    from google.genai import types
    import io
    import httpx

    client = genai.Client()

    long_context_pdf_path = "YOUR_LARGE_PDF_URL"
    doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content) # Get PDF as bytes

    # Upload the PDF using the File API
    sample_doc = client.files.upload(
        path=doc_io,  # Can be a path or a file-like object
        config=dict(mime_type='application/pdf') # Required if using a file-like object
    )

    prompt = "Summarize this document"
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[sample_doc, prompt]  # Use the uploaded file object
    )
    print(response.text)
    ```
     *  Locally Stored.
    ```python
    from google import genai
    from google.genai import types
    import pathlib
    import httpx

    client = genai.Client()

    long_context_pdf_path = "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"

    # Retrieve the PDF
    file_path = pathlib.Path('A17.pdf')
    file_path.write_bytes(httpx.get(long_context_pdf_path).content)

    # Upload the PDF using the File API
    sample_file = client.files.upload(
      path=file_path,
    )

    prompt="Summarize this document"

    response = client.models.generate_content(
      model="gemini-1.5-flash",
      contents=[sample_file, "Summarize this document"])
    print(response.text)
    ```

FILE API OPERATIONS:

*   **`client.files.upload(path, config)`:** Uploads a file.  `path` can be a file path (string or `pathlib.Path`) or a file-like object (e.g., `io.BytesIO`).  If using a file-like object, you *must* provide the `mime_type` in the `config`.
*   **`client.files.get(file_name)`:** Retrieves metadata about an uploaded file (name, display name, size, etc.).  You *cannot* download the file content.  Only the `name` (and therefore the `uri`) is unique.
*   **`client.files.list()`:** Lists all uploaded files (within the 48-hour storage window).
*   **`client.files.delete(file_name)`:** Deletes an uploaded file.  Files are automatically deleted after 48 hours.

MULTIPLE PDFS:

*   You can process multiple PDFs in a *single* request, as long as the total size (PDFs + prompt) stays within the model's context window.  Use the File API for this.
* Example in the original document shows uploading two PDFs via URLs and then prompting the model to compare them.

CONTEXT CACHING:
*  It is possible to create, list, update and delete a cache.
* The objective is to reuse a file for different tasks.

WHAT'S NEXT:

*   **File Prompting Strategies:**  The Gemini API also supports other multimodal inputs (images, audio, video).
*   **System Instructions:**  Use system instructions to guide the model's overall behavior.
*   **Safety Guidance:**  Be aware of potential issues with generative AI outputs (inaccuracy, bias, offensive content) and implement mitigation strategies (post-processing, human review).

KEY TAKEAWAYS:

*   The Gemini API can directly process PDFs, understanding both text and visual content.
*   Use inline data for small PDFs (<20MB) and the File API for larger PDFs or when the total request size exceeds 20MB.
*   The File API provides temporary storage (48 hours) for uploaded files.
*   You can process multiple PDFs in a single request.
*   Be mindful of the technical details (page limits, token equivalence, image resolution handling).
* Leverage the File API to cache.

This `details.md` provides a comprehensive guide to using the Gemini API's PDF processing capabilities, including code examples, explanations of different input methods, details on the File API, and important considerations for working with PDFs. It's suitable for developers who want to integrate PDF processing into their applications using the Gemini API.