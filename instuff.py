import datetime
import scrapewat
import termOptions
import usrtable

now = datetime.datetime.now()

#Main class object that defines all of users core data points
#note the space variable is asking "Is there space?" and it will always default to True
class UserBlock:
    def __init__(self):
        self.code = None
        self.num = None
        self.sec = None
        self.term = None
        self.url = None
        self.coursestring = None
        self.email = None
        self.phone = None
        self.loginCode = None
        self.space = True

def functiontest():
    print("Testing backend app logic")
    usr = UserBlock()
    usr.code = "CS"
    usr.num = "115"
    usr.sec = "001"
    usr.phone = "+15064250651"
    print("Displaying available terms: ")
    termOptions.displayOptions()
    uinput = input()
    usr.term = termOptions.termselect(uinput)
    usr = scrapewat.generateURL(usr)
    print(usr.coursestring)
    scrapewat.spacecheck(usr)
    usrtable.savetoDB(usr)

functiontest()
