OpenAI Audio Insight API

The OpenAI Audio Insight API allows users to analyze audio files, providing transcriptions and sentiment evaluations. The API leverages OpenAI's powerful language models for accurate and insightful results.
Getting Started
Prerequisites

Make sure you have the following prerequisites before using the OpenAI Audio Insight API:

    Python installed on your machine
    OpenAI API key

Installation

    Clone the repository:

    bash

git clone https://github.com/your-username/openai-audio-insight-api.git
cd openai-audio-insight-api

Install dependencies:

bash

pip install -r requirements.txt

Set your OpenAI API key:

bash

    export OPENAI_API_KEY=your-api-key

Usage

    Add your audio files to the resources/ directory.

    Run the API:

    bash

python audio_api.py

Access the API:

    Open your browser and go to http://127.0.0.1:5000/

    Use the following curl command for analysis:

    bash

        curl -X POST -H "Content-Type: application/json" -d '{"file_path": "path/to/your/audio/file.mp3"}' http://127.0.0.1:5000/analyze

API Endpoints
POST /analyze

Analyzes the provided audio file and returns a JSON response with transcription and sentiment evaluation.
Request Body

json

{
  "file_path": "path/to/your/audio/file.mp3"
}

Response

json

{
  "transcript": "Transcription of the audio content.",
  "model_evaluation": "Sentiment evaluation based on the audio content."
}

Available Audio Files

Upon running the API, it will list all available audio files in the resources/ directory, prompting the user to select a file for analysis.
User Interaction

The API allows for user interaction, prompting the user to select an audio file, analyzing it, and providing the option to analyze additional files.
See You Soon!

Feel free to explore the capabilities of the OpenAI Audio Insight API. If you have any questions or feedback, please let us know. See you SpaceCowboy!