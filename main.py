from gtts import gTTS
from playsound import playsound
import random
import speech_recognition as sr
import os 
from difflib import SequenceMatcher
from createvocab import vocab

choice = "invalid"
while choice == "invalid":
    spanOrEnglish = input("Would you like to translate to spanish or english? (s/e): ")

    if spanOrEnglish == "s":
        print("Spanish mode selected.")
        mode = "spanish"
        choice = "valid"

    elif spanOrEnglish == "e" :
        print("English mode selected.")
        mode = "english"
        choice = "valid"

    else:
        print("Invalid input.")
        choice = "invalid"

amountOfWords = input("\nHow many words would you like to learn (a for all): ")

if amountOfWords == "a":
    amountOfWords = len(vocab)

#Function to check similarity of words
def check_similarity(lanugageWord, text):
  similarity = (SequenceMatcher(None, lanugageWord, text).ratio())
  if similarity >= 0.46:
    print("Correct!")
  elif text == "default":
    print("No input detected. The correct answer is " + lanugageWord + ".")
  else:
    print("Incorrect. The correct answer is " + lanugageWord + ". You said " + text + ".")

completedWords = []
wordsDone = 0

for spanishWord, englishWord in vocab.items():
    if englishWord not in completedWords and spanishWord not in completedWords and wordsDone < int(amountOfWords):
        if mode == "english":
            # Text to speech for Spanish
            tts = gTTS(text=spanishWord, lang="es")
            tts.save("current.mp3")
            playsound("current.mp3")
            os.remove("current.mp3")

            # Recognize speech for English
            r = sr.Recognizer()
            text = "default"

            with sr.Microphone() as source:
                try:
                    audio = r.listen(source)
                    text = r.recognize_google(audio)
                except:
                    pass

            check_similarity(englishWord, text)

        elif mode == "spanish":
            tts = gTTS(text=englishWord, lang="en")
            tts.save("current.mp3")
            playsound("current.mp3")
            os.remove("current.mp3")

            # Recognize speech for English
            r = sr.Recognizer()
            text = "default"

            with sr.Microphone() as source:
                try:
                    audio = r.listen(source)
                    text = r.recognize_google(audio, language="es-US")
                except:
                    pass

            check_similarity(spanishWord, text)

        completedWords.append(englishWord)
        completedWords.append(spanishWord)
        wordsDone += 1    