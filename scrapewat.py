import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import sendmail
import texter

now = datetime.datetime.now()

def generateURL(usr):
    usr.coursestring = usr.code + " " + usr.num
    usr.url = "http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=" + usr.term + "&subject=" + usr.code + "&cournum=" + usr.num
    return(usr)

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

def spacecheck(usr):
    df = scrapeTable(usr.url)
    selectedRow = df[df['Comp Sec'].str.contains(usr.sec)]
    cap = selectedRow['Enrl Cap'].astype(int)
    tot = selectedRow['Enrl Tot'].astype(int)
    diff = cap.iloc[0] - tot.iloc[0]
    print()
    if diff != 0 and usr.space != False:
        message = "There are " + str(diff) + " spots open in " + usr.coursestring
        print(message)
        #sendmail.emailNotification(emailAddr,courseString)
        texter.sendtext(usr.phone,message)
        usr.space = True
    elif diff == 0:
        print("No spots currently open in " + usr.coursestring +", will try again later")
        usr.space = False
        #setSpaceAvail(id,spaceAvail)
    else:
        print("Already notified for " + usr.coursestring)
