import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import sendmail
import dbSetter

def scrapeTable(url):
    #load and scrape
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    table = soup.table
    subtable = table.table
    dfs = pd.read_html(subtable.prettify(),header=0,flavor='bs4')
    df = dfs[0]
    return df

def loadVars():
    conn = dbSetter.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CourseWatchData;")
    watchlist = cursor.fetchall()
    conn.close()
    return watchlist

def setSpaceAvail(id,spaceAvail):
    conn = dbSetter.connect()
    cursor = conn.cursor()
    if spaceAvail == True:
        cursor.execute("UPDATE CourseWatchData set spaceAvail = 'Yes' WHERE entryID =" + str(id) + ";")
    if spaceAvail == False or spaceAvail == None:
        cursor.execute("UPDATE CourseWatchData set spaceAvail = 'No' WHERE entryID =" + str(id) + ";")
    conn.commit()
    conn.close()

def notifier(id,courCode,courNum,section,emailAddr,spaceAvail):
    #notifSent = 0
    courseString = courCode + " " + courNum
    url = "http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=1185&subject=" + courCode + "&cournum=" + courNum
    df = scrapeTable(url)

    selectedRow = df[df['Comp Sec'].str.contains(section)]
    cap = selectedRow['Enrl Cap'].astype(int)
    tot = selectedRow['Enrl Tot'].astype(int)
    diff = cap.iloc[0] - tot.iloc[0]
    print()
    if diff != 0 and spaceAvail != 'Yes':
        print("There are " + str(diff) + " spots open in " + courseString)
        sendmail.emailNotification(emailAddr,courseString)
        spaceAvail = True
        setSpaceAvail(id,spaceAvail)
    elif diff == 0:
        print("No spots currently open in " + courseString +", will try again later")
        spaceAvail = False
        setSpaceAvail(id,spaceAvail)
    else:
        print("Already notified for " + courseString)

while(True):
    watchlist = loadVars()
    for item in watchlist:
        id = item[0]
        email = item[2]
        courCode = item[4]
        courNum = item[5]
        section = item[6]
        spaceAvail = item[7]
        notifier(id,courCode,courNum,section,email,spaceAvail)
