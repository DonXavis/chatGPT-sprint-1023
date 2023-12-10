#!/usr/bin/env python3

import os
from openai import OpenAI
from dotenv import load_dotenv

class AudioAnalysis:
    """A class for audio analysis using the OpenAI API."""

    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Retrieve the OPENAI_API_KEY environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")

        # Set the retrieved API key for the OpenAI library
        OpenAI.api_key = self.api_key

        # Directory path for audio files
        self.media_path = "resources/"

    def show_audio_with_controls(self, file_path):
        """
        Display audio controls in Jupyter Notebook.

        Args:
        - file_path (str): Path to the audio file.
        """
        from IPython.display import HTML, display
        display(HTML("<audio controls><source src={} type='audio/mpeg'></audio>".format(file_path)))

    def analyze_audio(self, file_path):
        """
        Analyze audio file using the OpenAI API.

        Args:
        - file_path (str): Path to the audio file.
        """
        # Show audio controls
        self.show_audio_with_controls(file_path)

        # Get transcript
        transcript = OpenAI.audio.transcriptions.create(
            model="whisper-1",
            file=open(file_path, "rb"),
            language="en"
        )

        # Display transcript
        print("Transcript:", transcript.text)

        # Evaluate sentiment
        evaluation_response = OpenAI.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "You are a skilled Message evaluator."},
                {"role": "user", "content": f"Evaluate the following text sentiment:\n\n{transcript.text}"}
            ]
        )

        # Display model evaluation
        model_response = evaluation_response.choices[0].message.content
        print(f"Model Evaluation: {model_response}")

# If you need to test or use this directly, you can do:
# if __name__ == "__main__":
#     audio_analysis = AudioAnalysis()
#     audio_analysis.analyze_audio("your_audio_file.mp3")
