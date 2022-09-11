import random
import pyttsx3
from newsapi import NewsApiClient
# var = random.randint(1,6)
# print(var)
# list=["no lies","my daily life","tonikawa","AC/DC"]
# random.shuffle(list)
# print(list)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)
engine.say("hello sir how are you ")
news = NewsApiClient(api_key='1209b95504064ad993abfdcaa709474c')
top_hedlines =news.get_top_headlines(sources='bbc-news',
                                    language='en')

engine.say(news.get_sources())
engine.runAndWait()