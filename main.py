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

choice = "invalid"
while choice == "invalid":
    amountOfWords = input("\nHow many words would you like to learn (a for all): ")

    if amountOfWords == "a":
        amountOfWords = len(vocab)
        choice = "valid"
    elif amountOfWords.isnumeric() == False:
        print("Invalid input.")
        choice = "invalid"
    elif amountOfWords.isnumeric() == True:
        choice = "valid"

#Function to check similarity of words
def check_similarity(lanugageWord, text):
  '''Checks if your answer is correct based off how similar it is to the correct answer'''
  similarity = (SequenceMatcher(None, lanugageWord, text).ratio())
  if similarity >= 0.46:
    print("Correct!")
    text_to_speech("Correct!", "en")
  elif text == "default":
    print("No input detected. The correct answer is " + lanugageWord + ".")
    text_to_speech("No input detected. The correct answer is " + lanugageWord + ".", "en")
  else:
    print("Incorrect. The correct answer is " + lanugageWord + ". You said " + text + ".")
    text_to_speech("Incorrect. The correct answer is " + lanugageWord + ". You said " + text + ".", "en")

def text_to_speech(text, lang):
    '''Converts text to speech'''
    tts = gTTS(text=text, lang=lang)
    tts.save("current.mp3")
    playsound("current.mp3")
    os.remove("current.mp3")

#Initialize variables for loop 
completedWords = []
wordsDone = 0

#Loop through vocab words
for spanishWord, englishWord in vocab.items():
    #Check if word has been done
    if englishWord not in completedWords and spanishWord not in completedWords and wordsDone < int(amountOfWords):
        if mode == "english":
            #Text to speech for Spanish
            text_to_speech(spanishWord, "es")

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

            #Recognize speech for English
            r = sr.Recognizer()
            text = "default"

            with sr.Microphone() as source:
                try:
                    audio = r.listen(source)
                    text = r.recognize_google(audio, language="es-US")
                except:
                    pass
            check_similarity(spanishWord, text)
        
        #Add words to completed list
        completedWords.append(englishWord)
        completedWords.append(spanishWord)
        wordsDone += 1    