from gtts import gTTS
from playsound import playsound
import random
import speech_recognition as sr
import os 
from difflib import SequenceMatcher

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

#Create dict of vocab words
vocab = {
    "abre (command)": "open",
    "acostarse (ue)": "to go to bed, to lie down",
    "acostumbrarse": "to get used to",
    "afeitarse": "to shave",
    "almorzar (ue)": "to have lunch, to eat lunch",
    "aquel, aquella (aquellos, aquellas)": "that (one) (those [ones])",
    "aquello": "that",
    "así": "thus, that way",
    "bañarse": "to bathe",
    "la boca": "mouth",
    "broncearse": "to tan",
    "caerse": "to fall (down)",
    "calmarse": "to calm down",
    "la cara": "face",
    "la cena": "dinner, supper",
    "cenar": "to have dinner, to have supper",
    "cepillarse": "to brush",
    "el cepillo": "brush",
    "el champú": "shampoo",
    "la cita": "appointment; date",
    "el codo": "elbow",
    "comerse": "to eat up",
    "la comida": "midday meal",
    "la comida rápida": "fast food",
    "el corazón": "heart",
    "la crema de afeitar": "shaving cream",
    "el cuello": "neck",
    "el cuerpo": "body",
    "cuidarse": "to take care of yourself",
    "dejar de": "to stop, to quit",
    "derecho, derecha": "right",
    "desayunar": "to have breakfast",
    "el desayuno": "breakfast",
    "descansar": "to rest, to relax",
    "desde luego": "of course",
    "el desodorante": "deodorant",
    "despedirse (i, i)": "to say goodbye",
    "despertarse (ie)": "to wake up",
    "di (command)": "say",
    "el diente": "tooth",
    "divertirse (ie, i)": "to have fun",
    "el doctor, la doctora": "doctor",
    "doler (ue)": "to hurt",
    "dormirse (ue, u)": "to fall asleep",
    "la ducha": "shower",
    "ducharse": "to shower",
    "el ejercicio": "exercise",
    "el enfermero, la enfermera": "nurse",
    "equivocarse": "to be mistaken",
    "ese, esa (esos, esas)": "that (one) (those [ones])",
    "eso": "that (neuter form)",
    "la espalda": "back",
    "el espejo": "mirror",
    "esperar": "to wait (for)",
    "este, esta (estos, estas)": "this (one) (these [ones])",
    "esto": "this (neuter form)",
    "el estómago": "stomach",
    "fumar": "to smoke",
    "la garganta": "throat",
    "el grifo": "faucet",
    "la gripe": "flu",
    "la guitarra": "guitar",
    "el hombro": "shoulder",
    "el inodoro": "toilet",
    "irse": "to leave, to go away",
    "izquierdo, izquierda": "left",
    "el jabón": "soap",
    "el lago": "lake",
    "el lavabo": "sink",
    "lavarse": "to wash",
    "la lengua": "tongue",
    "levantarse": "to get up",
    "llamarse": "to be called",
    "llevarse": "to get along",
    "el maquillaje": "makeup",
    "maquillarse": "to put on makeup",
    "la medicina": "medicine",
    "la nariz (pl. las narices)": "nose",
    "el niño, la niña": "child",
    "el oído (inner)": "ear",
    "el ojo": "eye",
    "olvidarse": "to forget",
    "la oreja (outer)": "ear",
    "el pecho": "chest",
    "peinarse": "to comb",
    "el peine": "comb",
    "el pelo": "hair",
    "pescar": "to fish",
    "pescar un resfriado": "to catch a cold",
    "el pez (pl. los peces)": "fish",
    "ponerse": "to put on",
    "preguntarse": "to wonder; to ask oneself",
    "preocuparse": "to worry",
    "quedarse": "to remain, to stay",
    "quemarse": "to get burned",
    "quitarse": "to take off",
    "el resfriado": "cold",
    "reunirse": "to get together",
    "la rodilla": "knee",
    "saca (command)": "stick out",
    "la salud": "health",
    "sentarse (ie)": "to sit down",
    "sentirse (ie, i)": "to feel",
    "siéntate (command)": "sit down",
    "tarde": "late",
    "la tina": "bathtub",
    "la toalla": "towel",
    "tócate (command)": "touch",
    "vestirse (i, i)": "to get dressed"
}

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