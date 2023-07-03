from flask import Flask, render_template, request
import streamlit as st
import requests
import whisper
import time
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <body>
            <h1>Audio Transcription</h1>
            <form action="/transcribe" method="post" enctype="multipart/form-data">
                <input type="file" name="audio_file" accept=".mp3,.wav">
                <input type="submit" value="Transcribe">
            </form>
        </body>
    </html>
    '''

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio_file = request.files['audio_file']

    if audio_file is not None:
        file_name = audio_file.filename
        file_extension = file_name.split(".")[-1]
        destination_path = os.path.join(".", file_name)

        with open(destination_path, "wb") as f:
            f.write(audio_file.read())

        #version = st.selectbox("Select model type", ["tiny", "base", "small", "medium", "large"])
        model = whisper.load_model("medium")

        start_time = time.time()
        transcription = model.transcribe(file_name)
        end_time = time.time()

        transcribed_text = transcription["text"]
        elapsed_time = end_time - start_time

        return f'''
        <h2>Transcription Result:</h2>
        <h2>{transcribed_text}</h2>
        <h3>Elapsed Time: {elapsed_time} seconds</h3>
        '''

    else:
        return "Error: No audio file uploaded"
    
if __name__ == '__main__':
    app.run(debug=True)