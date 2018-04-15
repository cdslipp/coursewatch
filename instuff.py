import datetime
import scrapewat
import termOptions

now = datetime.datetime.now()

#Main class object that defines all of users core data points
#note the space variable is asking "Is there space?" and it will always default to True
class UserBlock:
    def __init__(self):
        self.code = ""
        self.num = ""
        self.sec = ""
        self.term = ""
        self.url = ""
        self.coursestring = ""
        self.email = ""
        self.phone = ""
        self.space = True

def functiontest():
    print("Testing backend app logic")
    usr = UserBlock()
    usr.code = "ECON"
    usr.num = "101"
    usr.sec = "001"
    usr.phone = "+15064250651"
    print("Displaying available terms: ")
    termOptions.displayOptions()
    uinput = input()
    usr.term = termOptions.termselect(uinput)
    usr = scrapewat.generateURL(usr)
    print(usr.coursestring)
    scrapewat.spacecheck(usr)

functiontest()
