import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import sendmail

now = datetime.datetime.now()

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

def termOptions():
    #This function creates an array that includes the current term and 1 future term
    terms = {}
    fullyear = now.year
    year = int(str(fullyear)[-2:])
    month = now.month
    for i in range(0,2):
        if i == 0:
            if month < 5:
                terms["Winter "+str(fullyear)]="1"+str(year)+"1"
            elif month < 9:
                terms["Spring "+str(fullyear)]="1"+str(year)+"5"
            else:
                terms["Fall "+str(fullyear)]="1"+str(year)+"9"
        if i == 1:
            if month < 5:
                terms["Spring "+str(fullyear)]="1"+str(year)+"5"
            elif month < 9:
                terms["Fall "+str(fullyear)]="1"+str(year)+"9"
            else:
                terms["Winter "+str(fullyear+1)]="1"+str(year+1)+"1"
    return terms

def generateURL(termCode,courCode,courNum,):
    courseString = courCode + " " + courNum
    url = "http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=" + termCode + "&subject=" + courCode + "&cournum=" + courNum
    print(url)
    return(url, courseString)

def notifier(id,url,section,emailAddr,spaceAvail,courseString):
    df = scrapeTable(url)
    selectedRow = df[df['Comp Sec'].str.contains(section)]
    cap = selectedRow['Enrl Cap'].astype(int)
    tot = selectedRow['Enrl Tot'].astype(int)
    diff = cap.iloc[0] - tot.iloc[0]
    print()
    if diff != 0 and spaceAvail != 'Yes':
        print("There are " + str(diff) + " spots open in " + courseString)
        #sendmail.emailNotification(emailAddr,courseString)
        spaceAvail = True
        #setSpaceAvail(id,spaceAvail)
    elif diff == 0:
        print("No spots currently open in " + courseString +", will try again later")
        spaceAvail = False
        #setSpaceAvail(id,spaceAvail)
    else:
        print("Already notified for " + courseString)

def termselect(userIn):
    #basic logic and input to test term selecter
    print("Select the term: ")
    termDict = termOptions()
    termList = list(termDict.keys())
    print("1 - " + termList[0])
    print("2 - " + termList[1])
    if userIn == "1":
        termString = termList[0]
    if userIn == "2":
        termString = termList[1]
    term = termDict.get(termString)
    return term

def functiontest():
    print("Testing backend app logic")
    courCode = "ECON"
    courNum = "101"
    term = termselect("2")
    print(term)
    url = generateURL(term,courCode,courNum)
    



functiontest()
