import datetime

now = datetime.datetime.now()

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

def displayOptions():
    #display the available terms
    print("Select the term: ")
    termDict = termOptions()
    termList = list(termDict.keys())
    print("1 - " + termList[0])
    print("2 - " + termList[1])

def termselect(userIn):
    #basic logic and input to test term selecter
    termDict = termOptions()
    termList = list(termDict.keys())
    if userIn == "1":
        termString = termList[0]
    if userIn == "2":
        termString = termList[1]
    term = termDict.get(termString)
    return term
