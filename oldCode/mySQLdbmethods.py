#Logic that was being used with PythonAnywhere mySQL instance

#Get DB table row
def loadVars():
    conn = dbSetter.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CourseWatchData;")
    watchlist = cursor.fetchall()
    conn.close()
    return watchlist

def setSpaceAvail(id,spaceAvail):
    conn = dbSetter.connect()
    cursor = conn.cursor()
    if spaceAvail == True:
        cursor.execute("UPDATE CourseWatchData set spaceAvail = 'Yes' WHERE entryID =" + str(id) + ";")
    if spaceAvail == False or spaceAvail == None:
        cursor.execute("UPDATE CourseWatchData set spaceAvail = 'No' WHERE entryID =" + str(id) + ";")
    conn.commit()
    conn.close()
