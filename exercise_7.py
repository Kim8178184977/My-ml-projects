import datetime
import pyttsx3
import time
import sys
org = sys.stdout
def date():
        return datetime.datetime.now()
while True:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',180)
    # this is the driver code from here
    
    
    engine.say("good morning sir please do some exercise")
    engine.runAndWait()
    time.sleep(2)
    with open ("exercise.txt",'a') as file:
        answer = input("\ninput here in done and no :- ")
        sys.stdout = file
        print(date())
        sys.stdout = org
    engine.say("good morning sir please do some water")
    engine.runAndWait()
    time.sleep(2)
    with open ("exercise.txt",'a') as file:
        answer = input("\ninput here in done and no :- ")
        sys.stdout = file
        print(date())
        sys.stdout = org
    engine.say("good morning sir please do some eye exercise")
    engine.runAndWait()
    time.sleep(2)
    with open ("exercise.txt",'a') as file:
        answer = input("\ninput here in done and no :- ")
        sys.stdout = file
        print(date())
        sys.stdout = org
        if answer == 'done':
            break