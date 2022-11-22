import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('listening..')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
except:
    pass
print("This will work today")