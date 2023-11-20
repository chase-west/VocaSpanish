from gtts import gTTS
from playsound import playsound
import random
import speech_recognition as sr
import os 
from difflib import SequenceMatcher
import time

spanOrEnglish = input("Would you like to translate to spanish or english? (s/e): ")
amountOfWords = input("How many words would you like to learn: ")

if spanOrEnglish == "s":
   mode = "spanish"

else :
   mode = "english"


#Create dict of vocab words
vocab = {
  "hello": "hola",
  "goodbye": "adiós",
  "good morning": "buenos días",
  "good afternoon": "buenas tardes",
  "good evening": "buenas noches",
  "how are you?": "¿cómo estás?",
  "good": "bien",
  "bad": "mal",
  "thank you": "gracias",
  "please": "por favor",
  "you're welcome": "de nada",
  "excuse me": "con permiso",
  "I'm sorry": "lo siento",
  "yes": "sí",
  "no": "no",
  "I don't understand": "no entiendo",
  "I don't know": "no sé",
  "what's your name?": "¿cómo te llamas?",
  "my name is": "me llamo",
  "where are you from?": "¿de dónde eres?",
  "I'm from": "soy de",
  "how old are you?": "¿cuántos años tienes?",
  "I'm": "tengo",
  "what time is it?": "¿qué hora es?",
  "it's": "son las",
  "what day is it?": "¿qué día es?",
  "today is": "hoy es",
  "tomorrow is": "mañana es",
  "yesterday was": "ayer fue",
  "what is this?": "¿qué es esto?",
  "this is": "esto es",
  "how much does it cost?": "¿cuánto cuesta?",
  "where is the bathroom?": "¿dónde está el baño?",
  "where is the bus stop?": "¿dónde está la parada de autobús?",
  "where is the train station?": "¿dónde está la estación de tren?",
  "where is the airport?": "¿dónde está el aeropuerto?",
  "where is the hotel?": "¿dónde está el hotel?",
  "where is the restaurant?": "¿dónde está el restaurante?",
  "where is the bank?": "¿dónde está el banco?",
  "where is the pharmacy?": "¿dónde está la farmacia?",
}

#Function to check if two strings are similar
def similarity(a, b):
  return (SequenceMatcher(None, a, b).ratio())


completedWords = []

while len(completedWords) <= int(amountOfWords):
  

  #Choose random word from dict
  for i in range(len(vocab)):
      englishWord, spanishWord = random.choice(list(vocab.items()))

      if englishWord not in completedWords and spanishWord not in completedWords:
          completedWords.append(englishWord)
          completedWords.append(spanishWord)
          break

  if mode == "english":
    #Text to speech for spanish 
    tts = gTTS(text=spanishWord, lang="es")
    tts.save("current.mp3")
    time.sleep(2)
    playsound("current.mp3")
    os.remove("current.mp3")

    #Recognize speech for english 
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
      print("Incorrect. The correct answer is " + englishWord + "." + " You said " + text + ".")
    completedWords.append(englishWord)
    completedWords.append(spanishWord)

  elif mode == "spanish":
    tts = gTTS(text=englishWord, lang="en")
    tts.save("current.mp3")
    playsound("current.mp3")
    os.remove("current.mp3")

    #Recognize speech for english 
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
      print("Incorrect. The correct answer is " + spanishWord + "." + " You said " + text + ".")
    completedWords.append(englishWord)
    completedWords.append(spanishWord)
    