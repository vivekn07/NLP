# pip3 install SpeechRecognition pydub

import speech_recognition as sr

filename = "myfile.wav"

# Initialize the recognizer
r = sr.Recognizer()

# Open the audio file
with sr.AudioFile(filename) as source:
    # Listen for the data (load audio to memory)
    audio_data = r.record(source)

    # Recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)