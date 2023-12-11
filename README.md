OpenAI Audio Analysis API

The OpenAI Audio Analysis API is a powerful tool for transcribing and analyzing audio files using state-of-the-art natural language processing and machine learning models. This API integrates the capabilities of the Whisper ASR model for transcription and the GPT-3.5-turbo model for sentiment analysis.
Features

    Audio Transcription: Utilize the Whisper ASR model to transcribe audio files into text.
    Sentiment Analysis: Evaluate the sentiment of the transcribed text using the GPT-3.5-turbo model.

Usage

    Set Up Your API Key:
        Obtain an API key from OpenAI and set it in the OPENAI_API_KEY variable.

    Provide Audio Files:
        Place your audio files in the "resources" folder.

    Run the API:
        Execute the provided script to interactively analyze and transcribe audio files.

    User Interaction:
        The API prompts the user to select an audio file and displays the transcribed text along with sentiment analysis results.

    Repeat or Exit:
        Users can choose to analyze additional files or exit the program.

Dependencies

    OpenAI Python Package
    IPython Widgets

Getting Started

    Install dependencies:

    bash

pip install openai ipywidgets

Set your OpenAI API key:

python

os.environ["OPENAI_API_KEY"] = "YOUR OPENAI_API_KEY"

Run the script:

bash

    python your_script_name.py

Note

Ensure that you comply with OpenAI's usage policies and guidelines while using this API.

Feel free to explore the capabilities of the OpenAI Audio Insight API. If you have any questions or feedback, please let us know. See you SpaceCowboy!