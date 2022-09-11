import datetime
from unittest import result
import wikipedia
import os
import spotipy
import smtplib
import pywhatkit
import pyttsx3
import speech_recognition as sr
from newsapi import NewsApiClient
from keyboard import press
from keyboard import press_and_release
from keyboard import write
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour <= 12:
        speak('Good morning sir')
    elif hour < 0 and hour > 14 :
        speak("good evening sir")
    else:
        speak("good evening sir")
    speak('tell me how can i assisst you today')

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.phrase_threshold = 0.5
        audio = r.listen(source)
        
    try:
        print('recognising....')
        query = r.recognize_google(audio, language= 'en-in')
        print(f'you said : {query}\n')
    except Exception as e:
        speak('sorry sir i did not understand')
        return None
    return query     

def email(to,content):
    mail_id = {'ashutosh':'ashu32696@gmail.com','ashutosh kumar':'ashu28jan2003@gmail.com','papa':'kumarivanee@gmail.com','mummy':'kumarivanee06@gmail.com'}
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ashu28jan2003@gmail.com','qehjvipittpmgzbe')
    to_send = mail_id.get(to)
    server.sendmail('ashu28jan2003@gmail.com',to_send,content)
    server.close()

def msg (number,message):
    dict =  {'me':'8178184977','papa':'7678480663'}
    contact = dict.get(number)
    hour = datetime.datetime.now().hour
    mnt = datetime.datetime.now().minute
    pywhatkit.sendwhatmsg(contact,message,hour,mnt,0)

def song (name):
    pass

def news (my_str):
    news = NewsApiClient(api_key='1209b95504064ad993abfdcaa709474c')
    if 'headlines' in my_str:
        top_headlines = news.get_top_headlines(sources='india today',language='en-in')
        news = top_headlines['articals']
        for headlines in news :
            speak(headlines)
    else:
        speak('there is some issue in serching for news')

def system_control (cmnd):
    if 'pause'in cmnd:
        press('space bar')
    elif 'play'in cmnd:
        press('space bar')
    elif 'full screen' in cmnd:
        press('f')
    elif 'minimise' in cmnd:
        press('i')
    elif 'next' in cmnd:
        press_and_release('shift'+'n')
    elif 'again' in cmnd:
        press_and_release('shift'+'p')
    elif 'new' in cmnd:
        press('/')
        speak('what you want to see')
        vid = command()
        pywhatkit.playonyt(vid)
        speak('as you wish sir')
    elif 'repeat' in quary:
        press('j')
    elif 'skip' in quary:
        press('l')
    elif 'mute' in quary:
        press ('m')

if __name__=='__main__':
    
    wish_me()
    while True:
    
        quary = command().lower()
        if 'wikipedia' in quary:
            speak('looking the results for your search ')
            quary = quary.replace('wikipedia', '')
            result = wikipedia.summary(quary, sentences = 2)
            speak('according to my search ')
            speak(result)
        elif 'youtube' in quary:
            speak('tell me what you want to see')
            video = command()
            pywhatkit.playonyt(video)
            speak('as you wish sir')
        elif 'google'in quary:
            speak('ok sir')
            quary = quary.replace('google','')
            result = pywhatkit.search(quary)
            speak(result)
        elif 'the time' in quary:
            speak(f'the time is {datetime.datetime.now().strftime("%H:%M")}')
        elif 'start project'in quary:
            codePath ='C:\\Users\\91817\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        elif 'email' in quary:
            try:
                speak('ok sir tell me the mail id of the person')
                key = command().lower()
                speak('tell me the content you want to put inside the mail')
                content = command()
                speak('task completed')
                email(key,content)
            except Exception as e:
                speak('I thinck there is an unexpected error accured')
        elif 'information' in quary:
            quary=quary.replace('information','')
            result = pywhatkit.info(quary,lines = 2)
            speak(result)
        elif    'whats app' in quary:
            quary = quary.replace('msg','')
            quary = quary.replace('whats app','')
            speak('whats the message you want me to deliver')
            message = command()
            msg = (quary,message)
        elif 'song' in quary:
            speak('tell me the name of the song you want to lissen')
            music = command()
            song(music)
        elif 'video' in quary:
            cmnd = quary
            system_control(quary)