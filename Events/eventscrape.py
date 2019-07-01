from bs4 import BeautifulSoup as bs
import requests
import urllib
import csv
import itertools as iter


allEvents = []
allDates = []

site = 'https://www.pes.edu/events/'
siteReq = requests.get(site)
siteHTML = bs(siteReq.content, 'html.parser')

# with open('events.html', 'w') as f:
#     f.write(str(siteHTML))
# f.close()

allEventTitles = siteHTML.findAll(class_='item-title')
allMonthTitles =siteHTML.findAll(class_='month')
allDayTitles =siteHTML.findAll(class_='day')
allTimeTitles=siteHTML.findAll(class_='event-time')

for box in allEventTitles:
    allEventHTML = box.findAll('a')
    for event in allEventHTML:
        event = list(event)
        for e in event:
            allEvents.append(e)

months=[]
for m in allMonthTitles:
    months.append(list(m))

days=[]
for d in allDayTitles:
    days.append(list(d))

times=[]
for t in allTimeTitles:
    times.append(list(t))

for (m,d,t) in iter.zip_longest(months,days,times):
    allDates.append(m[0]+' '+d[0]+' '+t[0])

with open('events.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(allEvents,allDates))
