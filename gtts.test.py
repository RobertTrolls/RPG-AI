from gtts import gTTS
import os

def text_to_speech(text):
    # Initialize gTTS with the text to convert
    speech = gTTS(text)

    # Save the audio file to a temporary file
    speech_file = 'speech.mp3'
    speech.save(speech_file)

    # Play the audio file
    os.system('afplay ' + speech_file)

text_to_speech('Hello, world! This is a test.')

def text_to_speech(text):
    # Initialize gTTS with the text to convert
    speech = gTTS(text, lang='en', slow=False, tld='com')

    # Save the audio file to a temporary file…
