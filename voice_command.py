import speech_recognition as sr
from datetime import datetime

print("=" * 60)
print("          VOICE COMMAND RECOGNITION")
print("=" * 60)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("\nListening...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio).lower()

    print("\nRecognized Command:", command)

    if "hello" in command:
        print("Response: Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        print("Current Time:", current_time)

    elif "help" in command:
        print("Available commands: hello, time, search, exit")

    elif "search" in command:
        print("Response: Search command recognized.")

    elif "exit" in command or "stop" in command:
        print("Response: Exiting voice assistant.")

    else:
        print("Response: Command not recognized.")

except sr.UnknownValueError:
    print("\nSorry, I could not understand the command.")

except sr.RequestError:
    print("\nSpeech recognition service is unavailable.")