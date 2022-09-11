import speech_recognition as sr
import pyttsx3
from newsapi import NewsApiClient
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)
recognising = sr.Recognizer()
with sr.Microphone() as sourse:
    print('listning.....')
    audio = recognising.listen(sourse,timeout=1)
    recognising.adjust_for_ambient_noise(sourse,duration=0.001)
try:
    # engine.say(f" ok i am showing you some {recognising.recognize_google(audio)}")
    news = NewsApiClient(api_key='1209b95504064ad993abfdcaa709474c')
    top_hedlines =news.get_top_headlines(sources='bbc-news',
                                        language='en')
    news = top_hedlines['articles']
    print(news)
    
    for hedlines in news:
        engine.say(hedlines['title'])

except sr.UnknownValueError:
    engine.say("I could not understand can you say it again")
except sr.RequestError as e:
    engine.say(f"search result 0.{format(e)}") 


engine.runAndWait()