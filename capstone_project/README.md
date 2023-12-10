OpenAI Audio Analysis with Jupyter Notebook
Overview

This project demonstrates how to perform audio analysis using the OpenAI API within a Jupyter Notebook environment. It includes functions for audio transcription and sentiment analysis using the Whisper ASR and GPT-3.5-turbo models, respectively.
Getting Started
Prerequisites

Before you begin, ensure you have the following:

    An OpenAI API key. Obtain one by signing up on the OpenAI website.
    Python installed on your system.

Installation

Install the required Python packages using the following command:

bash

pip install openai ipywidgets

OpenAI API Key Setup

Set your OpenAI API key as an environment variable. Replace "your_api_key_here" with your actual API key.

bash

export OPENAI_API_KEY=your_api_key_here

Usage

    Open the provided Jupyter Notebook (OpenAI_Audio_Analysis.ipynb) in your Jupyter environment.

    Run each cell sequentially to execute the code. The notebook guides you through the process of analyzing audio files step by step.

    Follow the instructions to select an audio file for analysis and review the transcription and sentiment analysis results.

    Optionally, you can analyze multiple audio files within the resources folder. The notebook will prompt you to decide whether to analyze another file after each execution.

Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please create an issue or submit a pull request.
License

This project is licensed under the MIT License.
Acknowledgments

    OpenAI for providing the powerful audio analysis capabilities.