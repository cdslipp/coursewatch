import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import sendmail

def sms_notification(message):
    report = {}
    report["value1"] = "From cloud instance" + str(message)
    requests.post("https://maker.ifttt.com/trigger/spot_open/with/key/L6S7Ci0nA0CKFAm9OiOZD", data=report)

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

def notifier(courCode,courNum,section,emailAddr):
    #DEF ALL VARIABLES
    notifSent = 0
    spaceAvail = False
    #courCode = "ECON"
    #courNum = "101"
    #section = "LEC 081"
    #emailAddr = "cdslipp@gmail.com"
    courseString = courCode + " " + courNum
    url = "http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=1185&subject=" + courCode + "&cournum=" + courNum

    while(notifSent < 5):
        df = scrapeTable(url)
        selectedRow = df[df['Comp Sec'].str.contains(section)]
        cap = selectedRow['Enrl Cap'].astype(int)
        tot = selectedRow['Enrl Tot'].astype(int)
        #cap = pd.to_numeric(cap, errors='ignore')
        #print("CAP" + str(type(cap)) + "TOT" + str(type(tot)))
        diff = cap.iloc[0] - tot.iloc[0]
        print()
        if diff != 0:
            print("cloud worked")
            print(str(diff) + " spots open")
            #sms_notification(diff)
            sendmail.emailNotification(emailAddr,courseString)
            notifSent += 1
        else:
            print("No spots currently open, trying again in 1 minute")
        time.sleep(60)
