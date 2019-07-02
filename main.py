import pandas as pd
import spacy as sp
import random
import nltk
from nltk.stem import WordNetLemmatizer
import datetime
import os

# nltk.download('popular', quiet=True)
# nltk.download('punkt')
# nltk.download('wordnet')
lemmer = WordNetLemmatizer()

nlp = sp.load('en_core_web_sm')

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
btNames = list(arch['Name'])
btDesg = list(arch['Designation'])
btEmail = list(arch['E-mail'])

cv = pd.read_csv(fileDir+'\civildata.csv')
cvNames = list(arch['Name'])
cvDesg = list(arch['Designation'])
cvEmail = list(arch['E-mail'])

cs = pd.read_csv(fileDir+'\csedata.csv')
csNames = list(arch['Name'])
csDesg = list(arch['Designation'])
csEmail = list(arch['E-mail'])

ec = pd.read_csv(fileDir+'\ecedata.csv')
ecNames = list(arch['Name'])
ecDesg = list(arch['Designation'])
ecEmail = list(arch['E-mail'])

ee = pd.read_csv(fileDir+'\eeedata.csv')
eeNames = list(arch['Name'])
eeDesg = list(arch['Designation'])
eeEmail = list(arch['E-mail'])

mech = pd.read_csv(fileDir+'\mechdata.csv')
mechNames = list(arch['Name'])
mechDesg = list(arch['Designation'])
mechEmail = list(arch['E-mail'])

sh = pd.read_csv(fileDir+'\s&hdata.csv')
shNames = list(arch['Name'])
shDesg = list(arch['Designation'])
shEmail = list(arch['E-mail'])

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


hello()
userResponse = input('Type Bye to exit\n')
userResponse = nlp(userResponse.lower())
words = [x.lemma_ for x in userResponse]

while('bye' not in words):
    if 'sup' in words or 'hello' in words or 'hey' in words or 'hi' in words:
        hello()

    elif 'be' in words or 'what' in words or 'which' in words or 'when' in words:
        # questions related to events occuring in college
        if 'event' in words or 'activity' in words or 'occur' in words:
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
                if hol[tomDateIndex] == 'Yes':
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

    else:
        print("I'm sorry, I didn't understand that.")
    userResponse = input()
    userResponse = nlp(userResponse.lower())
    words = [x.lemma_ for x in userResponse]
    # print(words)

bye()
