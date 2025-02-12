from google import genai
import os

# Tuned Model ID
tuned_model_id = '<YOUR_TUNED_MODEL_ID>' # Example: example-tuned-model-u1ry1ru5t4px

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Print a message if no models are found
if len(client.models.list()) == 0:
    print("No tuned models found, Please create one. Like on the example ``Create_Tuning_Model.py``.")
    quit()

# Replace with the actual model name obtained from the tuning job
tuned_model_name = f'tunedModels/{tuned_model_id}'

if tuned_model_name not in [model.name for model in client.models.list()]:
    print(f"{tuned_model_name} Tuned model not found.")
    quit()

# Generate the response
response = client.models.generate_content(
    model=tuned_model_name, # Use the tuned model
    contents='100'  # Example input
)

# Print the response
print(f"Response from tuned model: {response.text}")