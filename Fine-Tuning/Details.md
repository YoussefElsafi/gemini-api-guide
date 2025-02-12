--------------------------------------------------------------------------------
       Gemini API: Fine-Tuning (Conceptual Overview and Tutorial)
--------------------------------------------------------------------------------

OVERVIEW:

Fine-tuning is a process to improve the performance of Gemini API models on specific tasks by training them with a dataset of examples. It's useful when prompt engineering (e.g., few-shot prompting) is insufficient to achieve desired results, especially when you have a set of examples demonstrating the outputs you want. This document provides a conceptual overview and a practical tutorial using Python.

HOW FINE-TUNING WORKS:

1.  Goal: Enhance the model's performance for a particular task or enforce specific output requirements.

2.  Process: Provide the model with a training dataset containing examples of the task, structured as input-output pairs.

3.  Mechanism: The model learns additional parameters to encode the necessary information to perform the desired task or mimic the target behavior. This is known as supervised fine-tuning.

4.  Output: A new model is created, combining the newly learned parameters with the original model's parameters.

5.  Inference: Use the fine-tuned model at inference time to generate improved responses.

DATASET PREPARATION:

1.  Quality: Examples in the dataset should be of high quality, diverse, and representative of real-world inputs and outputs.

2.  Format:

    *   Must be input-output pairs (chat-style multi-turn conversations are *not* supported).
    *   Examples should match your expected production traffic in terms of formatting, keywords, instructions, and information.
    *   If your dataset includes a "question:" and a "context:", production traffic must also be formatted in the same way.
    *   Consider adding a prompt or preamble to each example in your dataset for improved performance; remember to include this preamble at inference time too.

    Example Dataset (Python, next number in sequence):

    ```python
    training_data = [
      {"text_input": "1", "output": "2"},
      {"text_input": "3", "output": "4"},
      {"text_input": "-3", "output": "-2"},
      {"text_input": "twenty two", "output": "twenty three"},
      # ... more examples ...
    ]
    ```

3.  Limitations (Gemini 1.5 Flash):

    *   Maximum input size per example: 40,000 characters.
    *   Maximum output size per example: 5,000 characters.

4.  Size:

    *   You can fine-tune with as few as 20 examples, but more data improves quality.
    *   Target between 100 and 500 examples, depending on the complexity of the task.
    *   Recommended dataset sizes for common tasks:

        *   Classification: 100+ examples
        *   Summarization: 100-500+ examples
        *   Document search: 100+ examples

5.  Upload:
   *  Data is either passed inline using the API. File size limit is 4 MB.

FINE-TUNING TUTORIAL (PYTHON):

1.  Prerequisites:

    *   Set up your Google Cloud project and enable the Gemini API.
    *   Obtain an API key.

2.  List Existing Tuned Models:

    ```python
    from google import genai
    client = genai.Client()

    for model_info in client.models.list():
        print(model_info.name)
    ```

3.  Create a Tuned Model:

    ```python
    from google import genai
    from google.genai import types

    client = genai.Client()

    # Training Data (Inline)
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
    training_dataset=types.TuningDataset(
            examples=[
                types.TuningExample(
                    text_input=i,
                    output=o,
                )
                for i,o in training_dataset
            ],
        )

    # Create Tuning Job
    tuning_job = client.tunings.tune(
        base_model='models/gemini-1.0-pro-001',  # Specify the base model
        training_dataset=training_dataset,
        config=types.CreateTuningJobConfig(
            epoch_count= 5,        #Number of times training data is ran through model.
            batch_size=4,          #Number of training examples in a single batch.
            learning_rate=0.001,  #Learning Rate.
            tuned_model_display_name="test tuned model"  #Descriptive Name.
        )
    )
    print(tuning_job)
    ```

4.  Generate Content with the Tuned Model:

    ```python
    response = client.models.generate_content(
        model=tuning_job.tuned_model.model, # use the model model name.
        contents='III',   # Test input
    )

    print(response.text)
    ```

ADVANCED TUNING SETTINGS:

*   **Epochs:** A full training pass over the entire training set.  Adjust based on the loss curve (see below).
*   **Batch Size:** The number of examples used in one training iteration.
*   **Learning Rate:** Controls how strongly the model adjusts its parameters in each iteration.

RECOMMENDED CONFIGURATIONS:

| Hyperparameter        | Default Value | Recommended Adjustments                                                                                                                                 |
| --------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Epoch Count           | 5             | Use a smaller value if the loss plateaus before 5 epochs. Use a higher value if the loss is converging and doesn't seem to plateau.               |
| Batch Size            | 4             |  Consider adjusting if memory constrains exist. |
| Learning Rate         | 0.001         | Use a smaller value for smaller datasets.                                                                                                             |

LOSS CURVE:

The loss curve shows the deviation between the model's predictions and the ideal predictions.  Ideally, stop training at the lowest point in the curve *before* it plateaus. The loss should not increase.

TROUBLESHOOTING:

1.  Authentication:
    *   Use API key authentication (recommended).
    *   If you encounter a `PermissionDenied` error, ensure proper authentication is set up.

2.  Canceled Models:
    *   The inference performance of a canceled model is unpredictable, especially if canceled early.
    *   If canceling to stop training at an earlier epoch, create a new tuning job with a lower epoch value.

LIMITATIONS OF TUNED MODELS:

*   Input limit (Gemini 1.5 Flash): 40,000 characters.
*   JSON mode is *not* supported.
*   Only text input is supported.

NEXT STEPS:

Explore the Python fine-tuning tutorial for a hands-on experience.

OTHER INFO.

* Not all function have been updated.