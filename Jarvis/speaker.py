from gtts import gTTS
import os
import sys

def say(text):
	tts = gTTS(text=text, lang='en-us')
	tts.save("sentence.mp3")
	os.system("mpg123 -q sentence.mp3")
	os.system("rm sentence.mp3")