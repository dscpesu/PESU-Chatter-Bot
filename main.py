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

def nameDetect(text):
    facList = []
    tempList = []
    nameList = []
    finalList = []
    name = ''
    text = text.replace("'", "")

    # formatting for extracting names
    if re.findall("Dr\.\s|Dr\.", text):
        text = re.sub("Dr\.\s|Dr\.", "Dr ", text)

    elif re.findall("Mr\.\s|Mr\.", text):
        text = re.sub("Mr\.\s|Mr\.", "Mr ", text)

    elif re.findall("Mrs\.\s|Mrs\.", text):
        text = re.sub("Mrs\.\s|Mrs\.", "Mrs ", text)

    elif re.findall("Ms\.\s|Ms\.", text):
        text = re.sub("Ms\.\s|Ms\.", "Ms ", text)

    elif re.findall("Prof\.\s|Prof\.", text):
        text = re.sub("Prof\.\s|Prof\.", "Prof ", text)

    elif re.findall("Ar\.\s|Ar\.", text):
        text = re.sub("Ar\.\s|Ar\.", "Ar ", text)

    # extracting the names
    for x in text.split():
        if re.findall("^[A-Z]", x):
            name = name+x+' '
            continue
        nameList.append(name)
        name = ''

    # formatting the names for database
    for x in nameList:

        if re.findall("Ar\s|Ar\s\s", x):
            tempList.append(re.sub("Ar\s|Ar\s\s", "Ar. ", x))
        elif re.findall("Dr\s|Dr\s\s", x):
            tempList.append(re.sub("Dr\s|Dr\s\s", "Dr. ", x))
        elif re.findall("Mr\s|Mr\s\s", x):
            tempList.append(re.sub("Mr\s|Mr\s\s", "Mr. ", x))
        elif re.findall("Ms\s|Ms\s\s", x):
            tempList.append(re.sub("Ms\s|Ms\s\s", "Ms. ", x))
        elif re.findall("Mrs\s|Mrs\s\s", x):
            tempList.append(re.sub("Mrs\s|Mrs\s\s", "Mrs. ", x))
        elif re.findall("Prof\s|Prof\s\s", x):
            tempList.append(re.sub("Prof\s|Prof\s\s", "Prof. ", x))

    for x in tempList:  # removes whitespaces at the end
        if re.findall("\s$", x):
            facList.append(re.sub("\s$", "", x))

    for x in facList:  # removes any s at the end if user gave a possessive noun
        if re.findall("s$", x):
            finalList.append(re.sub("s$", '', x))
            continue
        finalList.append(x)

    return finalList


def faculty(words, text, userResponse):
    facList = []
    facList = nameDetect(text)

    for x in facList:
        if ('mail' in words or 'e-mail' in words or 'email' in words) and ('designation'in words or 'job' in words or 'do' in words):
            if x in archNames:
                emIdx = archNames.index(x)
                return render_template('facultyEmail.html', x=x, email=archEmail[emIdx], desg=archDesg[emIdx], userResponse=userResponse)
            elif x in btNames:
                emIdx = btNames.index(x)
                return render_template('facultyEmail.html', x=x, email=btEmail[emIdx], desg=btDesg[emIdx], userResponse=userResponse)
            elif x in cvNames:
                emIdx = cvNames.index(x)
                return render_template('facDesg.html', x=x, email=cvEmail[emIdx], desg=cvDesg[emIdx], userResponse=userResponse)
            elif x in csNames:
                emIdx = csNames.index(x)
                return render_template('facDesg.html', x=x, email=csEmail[emIdx], desg=csDesg[emIdx], userResponse=userResponse)
            elif x in ecNames:
                emIdx = ecNames.index(x)
                return render_template('facDesg.html', x=x, email=ecEmail[emIdx], desg=ecDesg[emIdx], userResponse=userResponse)
            elif x in eeNames:
                emIdx = eeNames.index(x)
                return render_template('facDesg.html', x=x, email=eeEmail[emIdx], desg=eeDesg[emIdx], userResponse=userResponse)
            elif x in mechNames:
                emIdx = mechNames.index(x)
                return render_template('facDesg.html', x=x, email=mechEmail[emIdx], desg=mechDesg[emIdx], userResponse=userResponse)
            elif x in shNames:
                emIdx = shNames.index(x)
                return render_template('facDesg.html', x=x, email=shEmail[emIdx], desg=shDesg[emIdx], userResponse=userResponse)
            else:
                output = " does not seem to be a part of any department. You can ask for a list of the faculty under a certain department incase you aren't sure of the spelling. Please make sure the name is case-sensitive."
                return render_template('facultyError.html', x=x, output=output, userResponse=userResponse)

        if 'mail' in words or 'e-mail' in words or 'email' in words:
            if x in archNames:
                emIdx = archNames.index(x)
                return render_template('facultyEmail.html', x=x, email=archEmail[emIdx], userResponse=userResponse)
            elif x in btNames:
                emIdx = btNames.index(x)
                return render_template('facultyEmail.html', x=x, email=btEmail[emIdx], userResponse=userResponse)
            elif x in cvNames:
                emIdx = cvNames.index(x)
                return render_template('facultyEmail.html', x=x, email=cvEmail[emIdx], userResponse=userResponse)
            elif x in csNames:
                emIdx = csNames.index(x)
                return render_template('facultyEmail.html', x=x, email=csEmail[emIdx], userResponse=userResponse)
            elif x in ecNames:
                emIdx = ecNames.index(x)
                return render_template('facultyEmail.html', x=x, email=ecEmail[emIdx], userResponse=userResponse)
            elif x in eeNames:
                emIdx = eeNames.index(x)
                return render_template('facultyEmail.html', x=x, email=eeEmail[emIdx], userResponse=userResponse)
            elif x in mechNames:
                emIdx = mechNames.index(x)
                return render_template('facultyEmail.html', x=x, email=mechEmail[emIdx], userResponse=userResponse)
            elif x in shNames:
                emIdx = shNames.index(x)
                return render_template('facultyEmail.html', x=x, email=shEmail[emIdx], userResponse=userResponse)
            else:
                output = " does not seem to be a part of any department. You can ask for a list of the faculty under a certain department incase you aren't sure of the spelling. Please make sure the name is case-sensitive."
                return render_template('facultyError.html', x=x, output=output, userResponse=userResponse)

        if 'designation'in words or 'job' in words or 'do' in words:
            if x in archNames:
                emIdx = archNames.index(x)
                return render_template('facultyDesg.html', x=x, desg=archDesg[emIdx], userResponse=userResponse)
            elif x in btNames:
                emIdx = btNames.index(x)
                return render_template('facultyDesg.html', x=x, desg=btDesg[emIdx], userResponse=userResponse)
            elif x in cvNames:
                emIdx = cvNames.index(x)
                return render_template('facultyDesg.html', x=x, desg=cvDesg[emIdx], userResponse=userResponse)
            elif x in csNames:
                emIdx = csNames.index(x)
                return render_template('facultyDesg.html', x=x, desg=csDesg[emIdx], userResponse=userResponse)
            elif x in ecNames:
                emIdx = ecNames.index(x)
                return render_template('facultyDesg.html', x=x, desg=ecDesg[emIdx], userResponse=userResponse)
            elif x in eeNames:
                emIdx = eeNames.index(x)
                return render_template('facultyDesg.html', x=x, desg=eeDesg[emIdx], userResponse=userResponse)
            elif x in mechNames:
                emIdx = mechNames.index(x)
                return render_template('facultyDesg.html', x=x, desg=mechDesg[emIdx], userResponse=userResponse)
            elif x in shNames:
                emIdx = shNames.index(x)
                return render_template('facultyDesg.html', x=x, desg=shDesg[emIdx], userResponse=userResponse)
            else:
                if 'mail' not in words and 'e-mail' not in words and 'email' not in words:
                    output = " does not seem to be a part of any department. You can ask for a list of the faculty under a certain department incase you aren't sure of the spelling. Please make sure the name is case-sensitive."
                    return render_template('facultyError.html', x=x, output=output, userResponse=userResponse)


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

    elif 'be' in words or 'what' in words or 'which' in words:
        # questions related to events occuring in college
        if (user.similarity(eventComp[0]) > 0.85 or user.similarity(eventComp[1]) > 0.85) and 'event' in words:
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
        elif re.search("Ar\.\s[a-zA-Z]+|Ar\.[a-zA-Z]+|Prof\.\s[a-zA-Z]+|Mr\.\s[a-zA-Z]+|Dr\.\s[a-zA-Z]+|Ms\.\s[a-zA-Z]+|Mrs\.\s[a-zA-Z]+|Prof\.[a-zA-Z]+|Mr\.[a-zA-Z]+|Dr\.[a-zA-Z]+|Ms\.[a-zA-Z]+|Mrs\.[a-zA-Z]+", text) or extract_names(text):
            temp = re.sub(
                "Ar\.\s[a-zA-Z]+|Ar\.[a-zA-Z]+|Prof\.\s[a-zA-Z]+|Mr\.\s[a-zA-Z]+|Dr\.\s[a-zA-Z]+|Ms\.\s[a-zA-Z]+|Mrs\.\s[a-zA-Z]+|Prof\.[a-zA-Z]+|Mr\.[a-zA-Z]+|Dr\.[a-zA-Z]+|Ms\.[a-zA-Z]+|Mrs\.[a-zA-Z]+", " ", text)
            if(nlp(temp).similarity(profComp[0]) > 0.7 or nlp(temp).similarity(profComp[1]) > 0.7):
                return faculty(words, text, userResponse)
            else:
                output = "I'm sorry, I didn't understand that."
                return render_template('index.html', userResponse=userResponse, output=output)
        else:
            output = "I'm sorry, I didn't understand that."
            return render_template('index.html', userResponse=userResponse, output=output)
