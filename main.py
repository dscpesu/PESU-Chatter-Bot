import pandas as pd
import spacy as sp
import random
import nltk
from nltk.stem import WordNetLemmatizer
import datetime
import re
import os
from spacy.matcher import Matcher
from flask import Flask, render_template, request
from fuzzywuzzy import process, fuzz
from nameExtract import extract_names

app = Flask(__name__)
app.debug = True

# nltk.download('popular', quiet=True)
# nltk.download('punkt')
# nltk.download('wordnet')
lemmer = WordNetLemmatizer()

nlp = sp.load('en_core_web_md')
matcher = Matcher(nlp.vocab)

pwd = os.getcwd()
fileDir = pwd+'\\Data\\Faculty\\CSVs'

# reads the events data
e = pd.read_csv('data\Events\events.csv')
eNames = list(e['Name'])
eTimes = list(e['Time'])

# reads the faculty data
arch = pd.read_csv(fileDir+'\Archdata.csv')
archNames = list(arch['Name'])
archDesg = list(arch['Designation'])
archEmail = list(arch['E-mail'])

bt = pd.read_csv(fileDir+'\Btdata.csv')
btNames = list(bt['Name'])
btDesg = list(bt['Designation'])
btEmail = list(bt['E-mail'])

cv = pd.read_csv(fileDir+'\civildata.csv')
cvNames = list(cv['Name'])
cvDesg = list(cv['Designation'])
cvEmail = list(cv['E-mail'])

cs = pd.read_csv(fileDir+'\csedata.csv')
csNames = list(cs['Name'])
csDesg = list(cs['Designation'])
csEmail = list(cs['E-mail'])

ec = pd.read_csv(fileDir+'\ecedata.csv')
ecNames = list(ec['Name'])
ecDesg = list(ec['Designation'])
ecEmail = list(ec['E-mail'])

ee = pd.read_csv(fileDir+'\eeedata.csv')
eeNames = list(ee['Name'])
eeDesg = list(ee['Designation'])
eeEmail = list(ee['E-mail'])

mech = pd.read_csv(fileDir+'\mechdata.csv')
mechNames = list(mech['Name'])
mechDesg = list(mech['Designation'])
mechEmail = list(mech['E-mail'])

sh = pd.read_csv(fileDir+'\s&hdata.csv')
shNames = list(sh['Name'])
shDesg = list(sh['Designation'])
shEmail = list(sh['E-mail'])

# reads calendar data
cal = pd.read_csv('data\Calendar\calendar.csv')
calDate = list(cal['Date'])
hol = list(cal['Holiday'])
res = list(cal['Result'])
holIdx = []  # list conataining indexes of when it is a holiday
for i in range(len(hol)):
    if hol[i] == 'Yes':
        holIdx.append(i)
resIdx = res.index('Yes')

hi = ['Hi there!', 'Hey!', 'Hello! How can i help you?',
      'Sup', 'What can I do for you?']
by = ['Bye!', 'See you!', 'Goodbye!', 'Have a nice day!']


def hello():
    return random.choice(hi)


def bye():
    return random.choice(by)


def sorry():
    return "I'm sorry. I didn't understand you"


def faculty(words, text, userResponse):
    facList = []
    if re.search("Mr\.|Ms\.|Ar\.|Prof\.|Dr\.|Mrs\.", text):
        text = re.sub("Mr\.|Ms\.|Ar\.|Prof\.|Dr\.|Mrs\.", "Dr. ", text)
    
    text=re.sub("^[a-z]",text[0].upper(),text)
    text=re.sub("^can|^Can","What ",text)

    facList = extract_names(text)

    for x in facList:
        l = []
        l.append(process.extractOne(x, archNames)[1])
        l.append(process.extractOne(x, btNames)[1])
        l.append(process.extractOne(x, cvNames)[1])
        l.append(process.extractOne(x, csNames)[1])
        l.append(process.extractOne(x, ecNames)[1])
        l.append(process.extractOne(x, eeNames)[1])
        l.append(process.extractOne(x, mechNames)[1])
        l.append(process.extractOne(x, shNames)[1])
        maxi = max(l)
        maxIdx = l.index(maxi)
        
        if maxi < 70:
            output = " does not seem to be a part of any department."
            return render_template('facultyError.html', x=x, output=output, userResponse=userResponse)

        if maxIdx == 0:
            name = process.extractOne(x, archNames)[0]
            emIdx = archNames.index(name)
            email = archEmail[emIdx]
            desg = archDesg[emIdx]
        elif maxIdx == 1:
            name = process.extractOne(x, btNames)[0]
            emIdx = btNames.index(name)
            email = btEmail[emIdx]
            desg = btDesg[emIdx]
        elif maxIdx == 2:
            name = process.extractOne(x, cvNames)[0]
            emIdx = cvNames.index(name)
            email = cvEmail[emIdx]
            desg = cvDesg[emIdx]
        elif maxIdx == 3:
            name = process.extractOne(x, csNames)[0]
            emIdx = csNames.index(name)
            email = csEmail[emIdx]
            desg = csDesg[emIdx]
        elif maxIdx == 4:
            name = process.extractOne(x, ecNames)[0]
            emIdx = ecNames.index(name)
            email = ecEmail[emIdx]
            desg = ecDesg[emIdx]
        elif maxIdx == 5:
            name = process.extractOne(x, eeNames)[0]
            emIdx = eeNames.index(name)
            email = eeEmail[emIdx]
            desg = eeDesg[emIdx]
        elif maxIdx == 6:
            name = process.extractOne(x, mechNames)[0]
            emIdx = mechNames.index(name)
            email = mechEmail[emIdx]
            desg = mechDesg[emIdx]
        elif maxIdx == 7:
            name = process.extractOne(x, shNames)[0]
            emIdx = shNames.index(name)
            email = shEmail[emIdx]
            desg = shDesg[emIdx]

        if ('mail' in words or 'e-mail' in words or 'email' in words) and ('designation'in words or 'job' in words or 'do' in words):
            return render_template('facDesg.html', x=name, email=email, desg=desg, userResponse=userResponse)
        if 'mail' in words or 'e-mail' in words or 'email' in words:
            return render_template('facultyEmail.html', x=name, email=email, userResponse=userResponse)
        if 'designation'in words or 'job' in words or 'do' in words:
            return render_template('facultyDesg.html', x=name, desg=desg, userResponse=userResponse)


userResponse = ''
text = ''
userResponse = 'Your response here.'
output = 'Chatbot response.'
words = ''


def start():
    return render_template('index.html', userResponse=userResponse, output=output)


hiComp = [nlp('hi'), nlp('sup')]
eventComp = [nlp("what events are occuring in college?"),
             nlp("let me know what events are going on in college")]
holidayComp = [nlp("what days are holidays?"), nlp("is tomorrow a holiday?")]
resultComp = [nlp("what days are results coming out?"),
              nlp("is tomorrow the results?")]
profComp = [nlp('what is email?'), nlp('what is job?')]


def main1():
    userResponse = request.form['userResponse']
    text = userResponse
    user = nlp(userResponse.lower())
    words = [x.lemma_ for x in user]

    if user.similarity(hiComp[0]) > 0.7 or user.similarity(hiComp[1]) > 0.7:
        output = hello()
        return render_template('index.html', output=output, userResponse=userResponse)

    elif 'bye' in words:
        output = bye()
        return render_template('index.html', output=output, userResponse=userResponse)

    # questions related to events occuring in college
    elif (user.similarity(eventComp[0]) > 0.85 or user.similarity(eventComp[1]) > 0.85) and 'event' in words:
        if eNames:
            output = "The following events are occuring: "
            return render_template('events.html', output=output, eNames=eNames, eTimes=eTimes, userResponse=userResponse)
        else:
            output = 'No events are going on currently.'
            return render_template('index.html', userResponse=userResponse, output=output)

    # questions related to holidays
    elif user.similarity(holidayComp[1]) > 0.85 and 'tomorrow' in words and 'holiday' in words:
        tomDateIndex = calDate.index(
            str(datetime.date.today()+datetime.timedelta(days=1)))
        if hol[tomDateIndex] == 'Yes' or (datetime.date.today()+datetime.timedelta(days=1)).strftime("%A") == 'Sunday':
            output = 'Yes, tomorrow is a holiday!'
            return render_template('index.html', userResponse=userResponse, output=output)
        else:
            output = 'Sorry, tomorrow is not a holiday'
            return render_template('index.html', userResponse=userResponse, output=output)

    elif user.similarity(holidayComp[0]) > 0.85 and 'holiday' in words:
        output = 'The following dates are upcoming holidays:'
        return render_template('holiday.html', calDate=calDate, holIdx=holIdx, output=output, userResponse=userResponse)

    # questions related to results release
    elif user.similarity(resultComp[1]) > 0.85 and 'tomorrow' in words and 'result' in words:
        tomDateIndex = calDate.index(
            str(datetime.date.today()+datetime.timedelta(days=1)))
        if res[tomDateIndex] == 'Yes':
            output = 'Yes, tomorrow the results will be released!'
            return render_template('index.html', userResponse=userResponse, output=output)
        else:
            output = 'The results will not be released tomorrow. They will be released on '
            return render_template('results.html', userResponse=userResponse, output=output, calDate=calDate, resIdx=resIdx)

    elif user.similarity(resultComp[0]) > 0.85 and 'result' in words:
        output = 'The results will be released on '
        return render_template('results.html', userResponse=userResponse, output=output, calDate=calDate, resIdx=resIdx)
    
    # questions related to faculty
    elif re.search("Ar\.\s[a-zA-Z]+|Ar\.[a-zA-Z]+|Prof\.\s[a-zA-Z]+|Mr\.\s[a-zA-Z]+|Dr\.\s[a-zA-Z]+|Ms\.\s[a-zA-Z]+|Mrs\.\s[a-zA-Z]+|Prof\.[a-zA-Z]+|Mr\.[a-zA-Z]+|Dr\.[a-zA-Z]+|Ms\.[a-zA-Z]+|Mrs\.[a-zA-Z]+", text) or nlp(text).similarity(profComp[0]) > 0.7 or nlp(text).similarity(profComp[1]) > 0.7:
        temp = re.sub(
            "Ar\.\s[a-zA-Z]+|Ar\.[a-zA-Z]+|Prof\.\s[a-zA-Z]+|Mr\.\s[a-zA-Z]+|Dr\.\s[a-zA-Z]+|Ms\.\s[a-zA-Z]+|Mrs\.\s[a-zA-Z]+|Prof\.[a-zA-Z]+|Mr\.[a-zA-Z]+|Dr\.[a-zA-Z]+|Ms\.[a-zA-Z]+|Mrs\.[a-zA-Z]+", " ", text)
        
        if(nlp(temp).similarity(profComp[0]) > 0.7 or nlp(temp).similarity(profComp[1]) > 0.7 or nlp(text).similarity(profComp[0]) > 0.7 or nlp(text).similarity(profComp[1]) > 0.7):
            return faculty(words, text, userResponse)
        else:
            output = "I'm sorry, I didn't understand that."
            return render_template('index.html', userResponse=userResponse, output=output)
    
    else:
        output = "I'm sorry, I didn't understand that."
        return render_template('index.html', userResponse=userResponse, output=output)
