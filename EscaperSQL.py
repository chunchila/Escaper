import sqlite3 as lite


def createRoomsDatabase():
    def sqlconnect(filename='test.db'):
        try:
            con = lite.connect(filename)
            return con
        except lite.Error as e:
            print("Connect To Sql Error :  ", e)

    def sqlcursor(con):
        cur = con.cursor()
        return cur

    def sqldroptable(tablename="Rooms"):
        cur.execute("DROP TABLE IF EXISTS " + tablename)
        con.commit()

    def sqlcreatetable(tableName="Rooms"):
        cur.execute(
            "CREATE TABLE if not EXISTS " + tableName + "(pId INTEGER PRIMARY KEY AUTOINCREMENT , address TEXT ,city TEXT ,company TEXT ,escapecard TEXT ,facebook TEXT ,favicon TEXT ,id TEXT ,link TEXT ,name TEXT ,people TEXT ,review_score TEXT ,roomescape_id TEXT ,selected TEXT ,tel TEXT ,trip TEXT , currDate TEXT , currTime TEXT)")

    try:
        con = sqlconnect()
        cur = sqlcursor(con)
        sqldroptable()
        sqlcreatetable()
        con.execute("VACUUM")


    except Exception as e:
        print(e)

    con.commit()

    if con:
        con.close()


def createRoomsDatesDatabase():
    def sqlconnect(filename='test.db'):
        try:
            con = lite.connect(filename)
            return con
        except lite.Error as e:
            print("Connect To Sql Error :  ", e)

    def sqlcursor(con):
        cur = con.cursor()
        return cur

    def sqldroptable(tablename="RoomDates"):
        cur.execute("DROP TABLE IF EXISTS " + tablename)
        con.commit()

    def sqlcreatetable(tableName="RoomDates"):
        cur.execute(
            "CREATE TABLE if not EXISTS " + tableName + "(pId INTEGER PRIMARY KEY AUTOINCREMENT , currDate TEXT , currTime TEXT ,roomDate TEXT,roomId TEXT , roomTimes TEXT)")

    try:
        con = sqlconnect()
        cur = sqlcursor(con)
        sqldroptable()
        sqlcreatetable()
        con.execute("VACUUM")


    except Exception as e:
        print(e)

    con.commit()

    if con:
        con.close()



createRoomsDatabase()
createRoomsDatesDatabase()
