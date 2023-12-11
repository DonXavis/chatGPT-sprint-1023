import os
from openai import OpenAI
from dotenv import load_dotenv

class ChatGPT:
    """A class to interact with OpenAI's ChatGPT model."""

    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Retrieve the OPENAI_API_KEY environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")

        # Set the retrieved API key for the OpenAI library
        self.client = OpenAI(api_key=self.api_key)

    def analyze_audio(self, file_path):

        # Get transcript
        transcript = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=open(file_path, "rb"),
            language="en"
        )

        # Display transcript
        print("Transcript:", transcript.text)

        # Evaluate sentiment
        evaluation_response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "You are a skilled Message evaluator."},
                {"role": "user", "content": f"Evaluate the following text sentiment:\n\n{transcript.text}"}
            ]
        )

        # Display model evaluation
        model_response = evaluation_response.choices[0].message.content
        print(f"Model Evaluation: {model_response}")
