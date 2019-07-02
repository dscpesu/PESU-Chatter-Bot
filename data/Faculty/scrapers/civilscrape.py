from bs4 import BeautifulSoup as bs
import requests
import urllib
import re
import csv

def cleanHTML(text):
    clean = re.compile('[<.*?>]')
    ans = re.sub(clean, '', text)
    return ans

names = []
desgs = []
email = []
for number in range(1, 3):
    site = 'https://faculty.pes.edu/department-civil' + '?page=' + str(number)
    siteReq = requests.get(site)
    siteHTML = bs(siteReq.content, 'html.parser')
    allTitles = siteHTML.findAll(class_ = 'courses-title')
    for box in allTitles:
        allProf = box.findAll('h2')
        allDesg = box.findAll('p')
        for prof in allProf:
            ourProf = ' '.join(prof.text.split())
            names.append(ourProf)
        for desgie in allDesg:
            ourDesg = ' '.join(desgie.text.split())
            desgs.append(ourDesg)
    allDesc = siteHTML.findAll(class_ = 'course-des')
    for desc in allDesc:
        allEmails = desc.findAll(class_ = 'email')  
        for nemail in allEmails:
            ourEmail = ' '.join(nemail.text.split())
            email.append(ourEmail)

n=['Name']
d=['Designation']
e=['E-mail']
with open('E:\collage\DSC_Project\PESU-Chatter-Bot\data\Faculty\CSVs\civildata.csv', 'w+') as f:
    writer = csv.writer(f)
    writer.writerows(zip(n,d,e))
    writer.writerows(zip(names, desgs, email))