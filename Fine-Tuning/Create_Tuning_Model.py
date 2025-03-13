from google import genai
from google.genai import types
import os

# API Key
API_KEY = os.environ["API_KEY"]
client = genai.Client(api_key=API_KEY)

# Training Data (Replace with your training data)
training_dataset =  [
    ["1", "2"],
    ["3", "4"],
    ["-3", "-2"],
    ["twenty two", "twenty three"],
    ["two hundred", "two hundred one"],
    ["ninety nine", "one hundred"],
    ["8", "9"],
    ["-98", "-97"],
    ["1,000", "1,001"],
    ["10,100,000", "10,100,001"],
    ["thirteen", "fourteen"],
    ["eighty", "eighty one"],
    ["one", "two"],
    ["three", "four"],
    ["seven", "eight"],
]

# Create a Tuned Model
training_dataset=types.TuningDataset(
        examples=[
            types.TuningExample(
                text_input=i,
                output=o,
            )
            for i,o in training_dataset
        ],
    )

# Create a Tuning Job
tuning_job = client.tunings.tune(
    base_model='models/gemini-1.5-flash-001-tuning', # Use the Gemini 1.5 Flash model as it supports Fine Tuning
    training_dataset=training_dataset, # Provide the training dataset
    config=types.CreateTuningJobConfig( # Configure the tuning job
        epoch_count= 5, # Set the number of training epochs
        batch_size=4, # Set the batch size
        learning_rate=0.001, # Set the learning rate
        tuned_model_display_name="Counting Model" # Set a name for the tuned model
    )
)

# Print the job information
print("Tuning job initiated:")
print(tuning_job) # Print the job information, including the tuned_model ID.