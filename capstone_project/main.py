import os
import ipywidgets as widgets
from openai import OpenAI
from IPython.display import HTML, Audio, display

# Set your OpenAI API key - DON'T FORGET TO DO IT
os.environ["OPENAI_API_KEY"] = "YOUR OPENAI_API_KEY"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set the directory path
media_path = "resources/"

# Function to show audio with controls
def show_audio_with_controls(file_path):
    display(HTML("<audio controls><source src={} type='audio/mpeg'></audio>".format(file_path)))

# Function to perform analysis for a given file
def analyze_audio(file_path):
    # Show audio controls
    show_audio_with_controls(file_path)

    # Get transcript
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=open(file_path, "rb"),
        language="en"
    )

    # Display transcript
    print("Transcript:", transcript.text)

    # Evaluate sentiment
    evaluation_response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a skilled Message evaluator."},
            {"role": "user", "content": f"Evaluate the following text sentiment:\n\n{transcript.text}"}
        ]
    )

    # Display model evaluation
    model_response = evaluation_response.choices[0].message.content
    print(f"Model Evaluation: {model_response}")
# List all available audio files
audio_files = [f for f in os.listdir(media_path) if f.endswith(".mp3")]

# Check if there are any audio files
if not audio_files:
    print("No audio files found in the 'resources' folder.")
else:
    print("Available audio files:")
    for i, audio_file in enumerate(audio_files):
        print(f"{i + 1}. {audio_file}")
# Loop for user interaction
while True:
    # Ask the user to select a file
    selected_index = int(input(f"\nWelcome to OPENAI Audio Insight Enter the number corresponding to the file to analyze (1-{len(audio_files)}): "))
    
    if 1 <= selected_index <= len(audio_files):
        selected_file = audio_files[selected_index - 1]
        selected_file_path = os.path.join(media_path, selected_file)

        # Analyze the selected audio file
        analyze_audio(selected_file_path)
    else:
        print("Invalid selection. Please enter a valid number.")
    
    # Ask if the user wants to analyze another file
    another_file = input("Do you want to analyze another file? (yes/no): ").lower()
    if another_file != 'yes':
        break

print("See you soon!")
