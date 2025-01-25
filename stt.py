import speech_recognition as sr

def Speak():
    
    recognizer = sr.Recognizer()  # for speech recognition we need to use recognizer

    # to use the mic as the source we need to write
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening... You can Speak now!")

        try:
            # to Capture the audio use audio type
            audio = recognizer.listen(source, timeout=10)
            print("Recognizing...")

            # the speech is recognize by Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
        except sr.RequestError as e:
            print(f"Request failed; {e}")
        except sr.WaitTimeoutError:
            print("No speech detected in the given time frame.")

Speak()
