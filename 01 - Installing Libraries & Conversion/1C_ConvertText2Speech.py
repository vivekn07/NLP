# Install the required packages
# pip install gtts
# pip install playsound

from gtts import gTTS
from playsound import playsound

mytext = "Welcome to Practical 1: Natural Language programming, Viveksingh"
language = "en"

# Create the gTTS object
Myobj = gTTS(text=mytext, lang=language, slow=False)

# Save the audio file
Myobj.save("myfile.mp3")

# Play the audio file
playsound("myfile.mp3")

print("Text converted into speech successfully")

