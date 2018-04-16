from pymongo import MongoClient
import datetime

def savetoDB(usr):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.coursewatch
    usrtable = db.usertable
    userinfo = {key:value for key, value in usr.__dict__.items() if not key.startswith('__') and not callable(key)}
    userinfo['date'] = datetime.datetime.utcnow()
    print(userinfo)
    usrtable.insert_one(userinfo).inserted_id
