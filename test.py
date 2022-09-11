import smtplib 
from email.mime.text import MIMEText

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.ehlo()
server.login('ashu28jan2003@gmail.com','qehjvipittpmgzbe')
msg = MIMEText("पंडित जी मेरा नाम कुमारी वाणी है  और मैं दिल्ली से हूँ, मुझे अपने बेटे के बारे में जानना है  मेरे बेटे की जन्मतिथि 28 जनवरी 2003 है, जन्म स्थान (सीतामढ़ी, बिहार) है और जन्म समय 3:40 सुबह है  पंडित जी मेरा बेटा कंप्यूटर साइंस से बीटेक कर रहा है। और वह artificial intelligence में रूचि रखता है पंडित जी मय ये जान न चती हू यह विषय उनके करियर के लिए अच्छा है, और क्या वह विदेश में बसने में सक्षम होंगे, और वे नौकरी पाने और बसने में सक्षम होंगे, और क्या वह लव मैरिज करेगा? अगर हाँ तो क्या उसका वैवाहिक जीवन ठीक रहेगा और क्या वह हमें देख पाएगा")
msg['Subject'] = 'padit ji namaste may apne bete ke bare may jaan na chah ti hu'
for i in range(100):
    server.sendmail('ashu28jan2003@gmail.com','goodlucktoday@gnttv.com',msg.as_string())

    print(i,"mail have been sent to ")
server.close()
