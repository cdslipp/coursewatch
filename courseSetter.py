from pymongo import MongoClient
import datetime

def newCourseSection():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.coursewatch
    courDB = db.classes
    courInfo = {}
    courInfo['code'] = "ECON"
    courInfo['num'] = "101"
    courInfo['sec'] = "001"
    courInfo['url']="http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=1185&subject=ECON&cournum=101"
    courInfo['date'] = datetime.datetime.utcnow()
    courDB.insert_one(courInfo).inserted_id
    print(courInfo)

newCourseSection()
