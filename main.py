import speech_recognition as sr
import pyttsx3
import os

speech = sr.Recognizer()

try:
	engine = pyttsx3.init()
except ImportError:
	print("Request driver is not found")
except RuntimeError:
	print("Driver fails to initiliase")

voices = engine.getProperty('voices')

for voice in voices:
	print(voice.id)

engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

rate = engine.getProperty('rate')
engine.setProperty('rate',rate)
engine.say("Hello")
engine.say("Good Morning")
engine.say("Thanks Shardul ")
engine.say("Leader")
engine.runAndWait()

def speak_test_cmd(cmd):
	engine.say(cmd)
	engine.runAndWait()

def read_voice_cmd():
	voice_text = ""
	print("Listening..")
	with sr.Microphone() as source:
		audio = speech.listen(source)
	try:
		voice_text = speech.recognize_google(audio)
	except sr.UnknownValueError:
		pass
	except sr.RequestError as e:
		print("Network Problem")
	return voice_text

if __name__ == '__main__':
	speak_test_cmd("Hello Mr.Abhinav This is Jarvis Your Artificial Intelligence")

	while True:
		voice_note = read_voice_cmd()
		print('cmd: {}'.format(voice_note))
		if 'hello' in voice_note:
			speak_test_cmd("Hello Abhinav How I can help you?")
			continue
		elif 'open' in voice_note:
			os.system('explorer C:\\ {}'.format(voice_note.replace('Open ','')))
			continue
		elif 'bye' in voice_note:
			speak_test_cmd("Bye Abhinav Happy to help you.Have a good day.")
			exit()	





