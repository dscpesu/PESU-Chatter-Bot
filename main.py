import pandas as pd
import spacy as sp
import random
import nltk
import datetime
import re
import os
from spacy.matcher import Matcher
import string

# nltk.download('popular', quiet=True)
# nltk.download('punkt')
# nltk.download('wordnet')

nlp = sp.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

pwd = os.getcwd()
fileDir = pwd+'\\Data\\Faculty\\CSVs'

e = pd.read_csv('Events\events.csv')
eNames = list(e['Name'])
eTimes = list(e['Time'])

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

cal = pd.read_csv('Calendar\calendar.csv')
calDate = list(cal['Date'])
hol = list(cal['Holiday'])
res = list(cal['Result'])
holIdx = []
for i in range(len(hol)):
    if hol[i] == 'Yes':
        holIdx.append(i)
resIdx = res.index('Yes')

hi = ['Hi there!', 'Hey!', 'Hello! How can i help you?',
      'Sup', 'What can I do for you?']
bye = ['Bye!', 'See you!', 'Goodbye!', 'Have a nice day!']


def hello():
    print(random.choice(hi))


def bye():
    print(random.choice(bye))


def sorry():
    print("I'm sorry. I didn't understand you")


def facultyNames(words):
    if 'architecture' in words or 'arch' in words or 'b.arch' in words:
        for x in archNames:
            print(x)
    elif 'bt' in words or 'biotechnology' in words:
        for x in btNames:
            print(x)
    elif 'cs' in words or 'computer' in words or 'cse' in words:
        for x in csNames:
            print(x)
    elif 'bt' in words or 'biotechnology' in words or 'biotech' in words:
        for x in btNames:
            print(x)
    elif 'ec' in words or 'electronics' in words or 'ece' in words:
        for x in ecNames:
            print(x)
    elif 'ee' in words or 'electrical' in words or 'eee' in words:
        for x in eeNames:
            print(x)
    elif 'mech' in words or 'mechanical' in words:
        for x in mechNames:
            print(x)
    elif 's&h' in words or ('science' in words and 'humanities in words') or 'sh' in words:
        for x in shNames:
            print(x)
    elif 'cv' in words or 'civil' in words:
        for x in cvNames:
            print(x)
    else:
        print("I couldn't understand which department you're talking about.")

def nameDetect(text):
    s = text.translate(str.maketrans('', '', string.punctuation))
    s = s.split()
    start = False
    name = ""
    tempList = []
    facList=[]

    for x in s:
        if x == 'Prof' or x == 'Dr' or x == 'Mr' or x == 'Mrs' or x == 'Ms' or x=='Ar':
            name = name+x+'.'
            start = True
            continue

        if start == True:
            if re.search("^[A-Z]", x):
                name = name+' '+x
            else:
                start = False
                tempList.append(name)
                name = ''

    for x in tempList:
        if re.findall("s$",x):
            facList.append(re.sub("s$",'',x))
            continue
        facList.append(x)
        
    return facList


def faculty(words, text):
    
    facList=nameDetect(text)
    if not facList:
        # spaces must be present after Prof. or Dr. etc in order to detect thr name
        print(
            "Please make sure the name you typed has a space after their respective title.")
        return

    for x in facList:
        if 'mail' in words or 'e-mail' in words or 'email' in words:
            if x in archNames:
                emIdx = archNames.index(x)
                print(x, ': ', archEmail[emIdx])
            elif x in btNames:
                emIdx = btNames.index(x)
                print(x, ': ', btEmail[emIdx])
            elif x in cvNames:
                emIdx = cvNames.index(x)
                print(x, ': ', cvEmail[emIdx])
            elif x in csNames:
                emIdx = csNames.index(x)
                print(x, ': ', csEmail[emIdx])
            elif x in ecNames:
                emIdx = ecNames.index(x)
                print(x, ': ', ecEmail[emIdx])
            elif x in eeNames:
                emIdx = eeNames.index(x)
                print(x, ': ', eeEmail[emIdx])
            elif x in mechNames:
                emIdx = mechNames.index(x)
                print(x, ': ', mechEmail[emIdx])
            elif x in shNames:
                emIdx = shNames.index(x)
                print(x, ': ', shEmail[emIdx])
            else:
                print(x, " does not seem to be a part of any department. You can ask for a list of the faculty under a certain department incase you aren't sure of the spelling. Please make sure the name is case-sensitive.")
        if 'designation'in words or 'job' in words or 'do' in words:
            if x in archNames:
                emIdx = archNames.index(x)
                print(x, ': ', archDesg[emIdx])
            elif x in btNames:
                emIdx = btNames.index(x)
                print(x, ': ', btDesg[emIdx])
            elif x in cvNames:
                emIdx = cvNames.index(x)
                print(x, ': ', cvDesg[emIdx])
            elif x in csNames:
                emIdx = csNames.index(x)
                print(x, ': ', csDesg[emIdx])
            elif x in ecNames:
                emIdx = ecNames.index(x)
                print(x, ': ', ecDesg[emIdx])
            elif x in eeNames:
                emIdx = eeNames.index(x)
                print(x, ': ', eeDesg[emIdx])
            elif x in mechNames:
                emIdx = mechNames.index(x)
                print(x, ': ', mechDesg[emIdx])
            elif x in shNames:
                emIdx = shNames.index(x)
                print(x, ': ', shDesg[emIdx])
            else:
                if 'mail' not in words and 'e-mail' not in words and 'email' not in words:
                    print(x, " does not seem to be a part of any department. You can ask for a list of the faculty under a certain department in case you aren't sure of the spelling.")


print('Type Bye to exit\n')
hello()
userResponse = input()
text = userResponse
userResponse = nlp(userResponse.lower())
words = [x.lemma_ for x in userResponse]

while('bye' not in words):
    if 'sup' in words or 'hello' in words or 'hey' in words or 'hi' in words:
        hello()

    elif 'be' in words or 'what' in words or 'which' in words:
        # questions related to events occuring in college
        if ('event' in words or 'activity' in words or 'occur' in words) and 'be' in words:
            if eNames:
                print("The following events are occuring: ")
                for i in range(len(eNames)):
                    print(eNames[i], 'occuring on', eTimes[i])
            else:
                print('No events are going on currently.')
        elif 'holiday' in words:  # questions related to holidays
            if 'tomorrow' in words:
                tomDateIndex = calDate.index(
                    str(datetime.date.today()+datetime.timedelta(days=1)))
                if hol[tomDateIndex] == 'Yes' or (datetime.date.today()+datetime.timedelta(days=1)).strftime("%A") == 'Sunday':
                    print('Yes, tomorrow is a holiday!')
                else:
                    print('Sorry, tomorrow is not a holiday')
            else:
                print('The following dates are upcoming holidays:')
                for i in holIdx:
                    print(calDate[i])
        elif 'result' in words:  # questions related to results release
            if 'tomorrow' in words:
                tomDateIndex = calDate.index(
                    str(datetime.date.today()+datetime.timedelta(days=1)))
                if res[tomDateIndex] == 'Yes':
                    print('Yes, tomorrow the results will be released!')
                else:
                    print(
                        'The results will not be released tomorrow. They will be released on: ', calDate[resIdx])
            else:
                print('The results will be released on: ', calDate[resIdx])
        # questions related to faculty
        elif re.search("Prof\.\s[a-zA-Z]+|Mr\.\s[a-zA-Z]+|Dr\.\s[a-zA-Z]+|Ms\.\s[a-zA-Z]+|Mrs\.\s[a-zA-Z]+|Prof\.[a-zA-Z]+|Mr\.[a-zA-Z]+|Dr\.[a-zA-Z]+|Ms\.[a-zA-Z]+|Mrs\.[a-zA-Z]+", text) and ('designation'in words or 'job' in words or 'do' in words or 'mail' in words or 'e-mail' in words or 'email' in words):
            faculty(words, text)
        elif 'be' in words and ('faculty' in words or 'department' in words or 'dept' in words):
            facultyNames(words)

    else:
        sorry()
    userResponse = input('\n')
    text = userResponse
    userResponse = nlp(userResponse.lower())
    words = [x.lemma_ for x in userResponse]
    # print(words)

bye()
