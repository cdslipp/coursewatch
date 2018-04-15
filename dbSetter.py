import MySQLdb

def connect():
    conn = MySQLdb.connect(host= "cdslipp.mysql.pythonanywhere-services.com",
                  user="cdslipp",
                  passwd="juniper123",
                  db="cdslipp$cwdb")
    return conn

def saveForm(courCode,courNum,section,emailAddr):
    conn = MySQLdb.connect(host= "cdslipp.mysql.pythonanywhere-services.com",
                  user="cdslipp",
                  passwd="juniper123",
                  db="cdslipp$cwdb")

    x = conn.cursor()

    sql = "INSERT INTO CourseWatchData (email, courCode, courNum, section) VALUES ( ' " + emailAddr + "', '" + courCode + "', '" + courNum + "', '" + section + "');"

    x.execute(sql)
    conn.commit()
    conn.close()