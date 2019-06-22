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
for number in range(1, 7):
    site = 'https://faculty.pes.edu/department-Computer%20Science' + '?page=' + str(number)
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
with open('cse.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(names, desgs, email))