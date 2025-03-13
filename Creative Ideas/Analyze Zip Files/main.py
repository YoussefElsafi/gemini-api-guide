import os
import zipfile
from google import genai
import shutil

# --- Options for file types (can be toggled) ---
INCLUDE_DOCS = True
INCLUDE_AUDIO = True
INCLUDE_IMAGES = True
INCLUDE_VIDEOS = True

# --- Customizable Supported File Types ---
SUPPORTED_FILE_TYPES = {
    "docs": {  # Grouped for easier management
        ".pdf": "application/pdf",
        ".js": "text/javascript",
        ".py": "text/x-python",
        ".txt": "text/plain",
        ".html": "text/html",
        ".css": "text/css",
        ".md": "text/md",
        ".csv": "text/csv",
        ".xml": "text/xml",
        ".rtf": "text/rtf",
    },
    "audio": {
        ".wav": "audio/wav",
        ".mp3": "audio/mp3",
        ".aiff": "audio/aiff",
        ".aac": "audio/aac",
        ".ogg": "audio/ogg",
        ".flac": "audio/flac",
    },
    "image": {
        ".png": "image/png",
        ".jpeg": "image/jpeg",
        ".jpg": "image/jpeg",  # Handle both .jpg and .jpeg
        ".webp": "image/webp",
        ".heic": "image/heic",
        ".heif": "image/heif",
    },
    "video": {
        ".mp4": "video/mp4",
        ".mpeg": "video/mpeg",
        ".mpg": "video/mpg", #Handle both .mpeg and .mpg
        ".mov": "video/mov",
        ".avi": "video/avi",
        ".flv": "video/x-flv",
        ".webm": "video/webm",
        ".wmv": "video/wmv",
        ".3gp": "video/3gpp",
    }
}



def generate_file_tree(root_path, indent=""):
    """Generates a tree-like file path structure recursively."""
    tree_structure = ""
    try:
        items = os.listdir(root_path)
    except OSError as e:
        return f"{indent}ERROR: Could not access directory {root_path}: {e}\n"

    for item in sorted(items):  # Sorted for consistent output
        item_path = os.path.join(root_path, item)
        if os.path.isfile(item_path):
            tree_structure += f"{indent}- {item}\n"
        elif os.path.isdir(item_path):
            tree_structure += f"{indent}+ {item}/\n"
            tree_structure += generate_file_tree(item_path, indent + "  ")
    return tree_structure


def get_supported_file_paths(root_path, include_docs=True, include_audio=True, include_images=True, include_videos=True):
    """Gets paths of supported files, categorized by type."""

    supported_files = {
        "docs": [],
        "audio": [],
        "image": [],
        "video": []
    }

    for root, _, files in os.walk(root_path):
        for file in files:
            file_path = os.path.join(root, file)
            base, ext = os.path.splitext(file)
            ext = ext.lower()

            if include_docs and ext in SUPPORTED_FILE_TYPES["docs"]:
                supported_files["docs"].append(file_path)
            if include_audio and ext in SUPPORTED_FILE_TYPES["audio"]:
                supported_files["audio"].append(file_path)
            if include_images and ext in SUPPORTED_FILE_TYPES["image"]:
                supported_files["image"].append(file_path)
            if include_videos and ext in SUPPORTED_FILE_TYPES["video"]:
                supported_files["video"].append(file_path)

    return supported_files

def upload_and_generate(file_paths, file_tree, user_input):
    """Uploads files to Gemini and generates content.

        Args:
          file_paths: a dictionary with file paths for each of the keys 'docs', 'audio',
           'image', and 'video'.
           user_input: The user's input prompt (text).
           file_tree: the result of generate_file_tree

        Returns:
            The Gemini API's response (text).  Prints errors and handles them.
    """
    try:
        client = genai.Client()
        uploaded_files = []
        #Flatten the files
        flat_files = []
        for i in file_paths.keys():
          for file in file_paths[i]:
            flat_files.append(file)

        for file_path in flat_files:
            _, ext = os.path.splitext(file_path)
            ext = ext.lower()
            mime_type = None

            # Find appropriate mime_type
            for category, types in SUPPORTED_FILE_TYPES.items():
               if ext in types:
                mime_type = types[ext]
                if isinstance(mime_type, list):
                    mime_type = mime_type[0] #Prioritize first element.
                break  # Important: Stop searching once a match is found

            if mime_type is None: #Sanity Check.
                print(f"Warning: Could not find mime_type {file_path}")
                continue

            try:
                with open(file_path, 'rb') as f:
                    uploaded_file = client.files.upload(
                        file=f,  # Corrected: Use 'file' parameter with file object
                        config=dict(mime_type=mime_type)
                    )
                    uploaded_files.append(uploaded_file)
            except Exception as e:
                print(f"Error uploading {file_path}: {e}")
                #  Continue to the next file. Don't halt on error.
                continue
        
        from google.genai import types

        # Construct the contents for Gemini API call
        contents = [f"User's Prompt:{user_input}", f"Zip file structure: {file_tree}"] + uploaded_files

        response = client.models.generate_content(
                model = "gemini-2.0-flash",
                contents = contents,
                config=types.GenerateContentConfig(
                    system_instruction="You are an AI that analyzes Zip files, and you analyze the contents of the zip file." # The system instruction input to the AI
                ),
        )
        return response.text


    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "" #Return empty.
    except genai.APIError as e:
        print("Gemini API returned an error:", e)
        if e.candidates:
            for candidate in e.candidates:
                if candidate.finish_reason:
                    print("Finish Reason:", candidate.finish_reason)
                if candidate.safety_ratings:
                    print("Safety Ratings:")
                    for rating in candidate.safety_ratings:
                        print(f"- {rating.category}: {rating.probability}")
        return "ERROR: Gemini API request failed (see above for details)."

def main():
    """Main function to handle user input and process the ZIP file."""

    zip_file_path = input("Enter the path to the ZIP file: ")

    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Extract to a temporary directory
            temp_dir = "extracted_files"  # Use a relative path
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir)  # Create directory if it doesn't exist
            zip_ref.extractall(temp_dir)

            # Generate file tree structure
            file_tree = generate_file_tree(temp_dir)
            print("\nFile Tree Structure:\n", file_tree)

            # Get supported file paths
            supported_files = get_supported_file_paths(temp_dir, INCLUDE_DOCS, INCLUDE_AUDIO, INCLUDE_IMAGES, INCLUDE_VIDEOS)
            print("\nSupported Files:")
            for category, files in supported_files.items():
                print(f"\n{category.capitalize()}:")
                for file_path in files:
                    print(f"  - {file_path}")
            user_input = input("\n Enter your prompt for gemini: ")
            response = upload_and_generate(supported_files,file_tree,user_input)
            print("\n Gemini API Response: \n", response)


    except FileNotFoundError:
        print(f"Error: ZIP file not found at '{zip_file_path}'")
    except zipfile.BadZipFile:
        print(f"Error: Invalid or corrupted ZIP file at '{zip_file_path}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Clean up: Delete the temporary directory
        if os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir)  # Use shutil.rmtree to remove the directory
            except OSError as e:
                print(f"Warning: Could not delete temp directory: {e}")


if __name__ == "__main__":
    main()