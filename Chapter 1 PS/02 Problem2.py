#install an external module and use it to perform an operation

import pyttsx3          #pyttsx3 is a (use - text to speech) library of python 

pyttsx3.speak("I will speak today")

engine = pyttsx3.init()
voices = engine.getProperty('voices')       # getting details of current voice
# engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female
engine.say("I love myself")
engine.runAndWait()
engine.stop()