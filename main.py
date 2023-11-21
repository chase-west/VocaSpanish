from gtts import gTTS
from playsound import playsound
import random
import speech_recognition as sr
import os 
from difflib import SequenceMatcher

spanOrEnglish = input("Would you like to translate to spanish or english? (s/e): ")

if spanOrEnglish == "s":
   print("Spanish mode selected.")
   mode = "spanish"

else :
   print("English mode selected.")
   mode = "english"

amountOfWords = input("\nHow many words would you like to learn (a for all): ")

#Create dict of vocab words
vocab = {
  "peinarse": "to comb",
  "este, esta (estos, estas)": "this (one) (these [ones])",
  "esto": "this (neuter form)",
  "quitarse": "to take off",
  "ducharse": "to shower",
  "desayunar": "to have breakfast",
  "el peine": "comb",
  "así": "thus, that way",
  "la tina": "bathtub",
  "la ducha": "shower",
  "despertarse (ie)": "to wake up",
  "lavarse": "to wash",
  "quemarse": "to get burned",
  "la toalla": "towel",
  "calmarse": "to calm down",
  "eso": "that (neuter form)",
  "la cena": "dinner, supper",
  "ese, esa (esos, esas)": "that (one) (those [ones])",
  "el jabón": "soap",
  "tarde": "late",
  "acostarse (ue)": "to go to bed, to lie down",
  "la comida": "midday meal",
  "el pelo": "hair",
  "el cepillo": "brush",
  "preocuparse": "to worry",
  "afeitarse": "to shave",
  "almorzar (ue)": "to have lunch, to eat lunch",
  "el lavabo": "sink",
  "desde luego": "of course",
  "el inodoro": "toilet"
}

if amountOfWords == "a":
    amountOfWords = len(vocab)

#Function to check if two strings are similar
def similarity(a, b):
  return (SequenceMatcher(None, a, b).ratio())


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

            similar = similarity(text, englishWord)
            print(similar)
            if similar >= 0.5:
                print("Correct!")
            elif text == "default":
                print("No input detected. The correct answer is " + englishWord + ".")
            else:
                print("Incorrect. The correct answer is " + englishWord + ". You said " + text + ".")

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
                    text = r.recognize_google(audio, language="es")
                except:
                    pass

            similar = similarity(text, spanishWord)
            print(similar)
            if similar >= 0.5:
                print("Correct!")
            elif text == "default":
                print("No input detected. The correct answer is " + spanishWord + ".")
            else:
                print("Incorrect. The correct answer is " + spanishWord + ". You said " + text + ".")

        completedWords.append(englishWord)
        completedWords.append(spanishWord)
        wordsDone += 1
    