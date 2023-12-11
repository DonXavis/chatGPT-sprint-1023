import os
from brain_module import ChatGPT

# Set the directory path
media_path = "resources/"

# List all available audio files
audio_files = [f for f in os.listdir(media_path) if f.endswith(".mp3")]

# Check if there are any audio files
if not audio_files:
    print("No audio files found in the 'resources' folder.")
else:
    print("Available audio files:")
    for i, audio_file in enumerate(audio_files):
        print(f"{i + 1}. {audio_file}")

# Initialize ChatGPT
chat_gpt = ChatGPT()

# Loop for user interaction
while True:
    # Ask the user to select a file
    selected_index = int(input(f"\nWelcome to OPENAI Audio Insight Enter the number corresponding to the file to analyze (1-{len(audio_files)}): "))
    
    if 1 <= selected_index <= len(audio_files):
        selected_file = audio_files[selected_index - 1]
        selected_file_path = os.path.join(media_path, selected_file)

        # Analyze the selected audio file
        chat_gpt.analyze_audio(selected_file_path)
    else:
        print("Invalid selection. Please enter a valid number.")
    
    # Ask if the user wants to analyze another file
    another_file = input("Do you want to analyze another file? (yes/no): ").lower()
    if another_file != 'yes':
        break

print("See you soon!")
