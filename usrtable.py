from pymongo import MongoClient
import datetime

def savetoDB(usr):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.coursewatch
    usrtable = db.usertable
    courDB = db.classes

    userinfo = {key:value for key, value in usr.__dict__.items() if not key.startswith('__') and not callable(key)}
    userinfo['date'] = datetime.datetime.utcnow()
    print(userinfo)
    usrtable.insert_one(userinfo).inserted_id
    urlDict = {'url':userinfo['url']}
    secDict = {'sec':userinfo['sec']}

#sleepy Cameron here, this logic is not right, need to figure out logic to say Course exists - section does
#not or course does not exist at all
    if db.classes.find_one(urlDict) == None:
        if db.classes.find_one(secDict) == None :
            print("Could not find section. Creating new course entry...")
            courinfo = {k: userinfo[k] for k in ('code', 'num', 'sec','url')}
            courinfo['date'] = datetime.datetime.utcnow()
            courDB.insert_one(courinfo).inserted_id
    else:
        print("course and section already exists")
