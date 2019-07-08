import pandas as pd
import spacy as sp
import random
import nltk
from nltk.stem import WordNetLemmatizer
import datetime
import re
import os
from spacy.matcher import Matcher

# nltk.download('popular', quiet=True)
# nltk.download('punkt')
# nltk.download('wordnet')
lemmer = WordNetLemmatizer()

nlp = sp.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

pwd = os.getcwd()
fileDir = pwd+'\\Data\\Faculty\\CSVs'

e = pd.read_csv('data\Events\events.csv')
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

cal = pd.read_csv('data\Calendar\calendar.csv')
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
by = ['Bye!', 'See you!', 'Goodbye!', 'Have a nice day!']


def hello():
    print(random.choice(hi))


def bye():
    print(random.choice(by))


def sorry():
    print("I'm sorry. I didn't understand you")


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


def faculty(words, text):
    facList = []

    facList = nameDetect(text)
    for x in facList:
        if 'mail' in words or 'e-mail' in words or 'email' in words:
            if x in archNames:
                emIdx = archNames.index(x)
                print(x, ': Email- ', archEmail[emIdx])
            elif x in btNames:
                emIdx = btNames.index(x)
                print(x, ': Email- ', btEmail[emIdx])
            elif x in cvNames:
                emIdx = cvNames.index(x)
                print(x, ': Email- ', cvEmail[emIdx])
            elif x in csNames:
                emIdx = csNames.index(x)
                print(x, ': Email- ', csEmail[emIdx])
            elif x in ecNames:
                emIdx = ecNames.index(x)
                print(x, ': Email- ', ecEmail[emIdx])
            elif x in eeNames:
                emIdx = eeNames.index(x)
                print(x, ': Email- ', eeEmail[emIdx])
            elif x in mechNames:
                emIdx = mechNames.index(x)
                print(x, ': Email- ', mechEmail[emIdx])
            elif x in shNames:
                emIdx = shNames.index(x)
                print(x, ': Email- ', shEmail[emIdx])
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
                    print(x, " does not seem to be a part of any department. You can ask for a list of the faculty under a certain department incase you aren't sure of the spelling.")


print("Type Bye to exit\n")
hello()
userResponse = input('')
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
        elif re.search("Prof\.\s[a-zA-Z]+|Mr\.\s[a-zA-Z]+|Dr\.\s[a-zA-Z]+|Ms\.\s[a-zA-Z]+|Mrs\.\s[a-zA-Z]+|Prof\.[a-zA-Z]+|Mr\.[a-zA-Z]+|Dr\.[a-zA-Z]+|Ms\.[a-zA-Z]+|Mrs\.[a-zA-Z]+", text):
            faculty(words, text)
        
        else:
            sorry()

    else:
        print("I'm sorry, I didn't understand that.")
    userResponse = input('\n')
    text = userResponse
    userResponse = nlp(userResponse.lower())
    words = [x.lemma_ for x in userResponse]
    # print(words)

bye()
