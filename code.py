
import speech_recognition as sr
r=sr.Recognizer()
print("Please provide input ")
with sr.Microphone () as source:
    audio=r.listen(source)
try:
    print("You said: "+r.recognize_google(audio))
except Exception:
    print("Sorry didn't hear repeat again")
