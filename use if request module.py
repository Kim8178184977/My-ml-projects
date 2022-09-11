import requests
#the bellow function is to pull any any request from any wed-site 
r = requests.get("https://dictionary-api.cambridge.org/")
#the code is a way to print the data pulled by the function
print(r.text)
#the bellow code is to get the status code of which help us to find out wether the the site requested task is done or not if not then why
print(r.status_code)
url = "https://www.wikipidea.com"
data = {'p1':2,'p2':4}
#the bellow function is to post or send any data to the provided url
r2=requests.post(url=url,data=data)
print(r.status_code)