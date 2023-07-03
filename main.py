import streamlit as st
import requests
import whisper
import time
import os

# def main():
#     # Set page title
#     )st.title("Audio Transcription")

#     # Create a file uploader
#     audio_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])

#     # Check if a file is uploaded
#     if audio_file is not None:
#         # Display a play button for the uploaded audio file
#         st.audio(audio_file)

#         # Add a button to start transcription
#         if st.button("Transcribe"):
#             # Open the uploaded audio file
#             with open(audio_file.name, "rb") as file:
#                 # Prepare the data to be sent to the GitHub repository
#                 files = {"audio_file": file}
#                 url = "https://github.com/ShivangSingh15/project_one/raw/main/whisper/transcribe.py"

#                 model = Whi
#                 transcription = transcribe(file, audio_file.name)

#                 # Send a POST request to the GitHub repository for transcription
#                 response = requests.post(url, files=files)

#                 # Display the transcription result from the response
#                 if response.status_code == 200:
#                     transcription = response.json()["transcription"]
#                     st.write("Transcription:")
#                     st.write(transcription)
#                 else:
#                     st.write("Error occurred during transcription.")
#                     st.write(response.status_code


# if __name__ == "__main__":
#     main()


st.title("Audio Transcription")
audio_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])

if audio_file is not None:
    file_name = audio_file.name
    file_extension = file_name.split(".")[-1]
    destination_path = os.path.join(".", file_name)

    with open(destination_path, "wb") as f:
        f.write(audio_file.read())

    st.write("File saved successfully.")

version = st.selectbox("Select model type", ["tiny", "base", "small", "medium", "large"])


model = whisper.load_model(version)
st.text("Whisper Model Loaded")





# if st.sidebar.button("Load Whisper Model"):
#     model = load_whisper_model()
#     st.sidebar.success("Whisper model loaded")

# def get_audio_file_details(file):
#     file_details = {"FileName":file.name, "FileType":file.type, "FileSize":file.size}
#     return file_details

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        start_time = time.time()
        st.sidebar.success("Transcribing Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        end_time = time.time()
        st.text(transcription["text"])
        st.text(end_time-start_time)
    else:
        st.sidebar.error("Upload audio file")

# st.sidebar.button("play Original audio final")
# st.audio(audio_file)


