import json
import ast
import re
import sqlite3 as lite
import datetime
import time


def gethebrew(hexname):
    return re.sub(r'\\u[0-9a-fA-F]{4}', lambda x: eval('"' + x.group() + '"'), hexname)


with open("esc.txt", "r") as f:
    html = f.read()

txtRooms = html.split("rooms={")
txtDates = html.split("dates={")
txtCities = html.split("cities={")
regionsCities = html.split("regions={")

roomsFinal = "{" + txtRooms[1].split("}};")[0] + "}}"  # split for json }};
citiesFinal = "{" + txtCities[1].split("}};")[0] + "}}"  # split for hashtable ]};
datesFinal = "{" + txtDates[1].split("]};")[0] + "]}"  # split for hashtable ]};
regionFinal = "{" + regionsCities[1].split("]}")[0] + "]}"  # split for hashtable ]};

try:
    roomsJson = json.loads(str(roomsFinal.replace('\\"\\', '\\')))
    citiesArr = json.loads(str(citiesFinal.replace('\\"\\', '\\')))
    datesArr = ast.literal_eval(str(datesFinal))
    regionsCitiesArr = ast.literal_eval(str(regionFinal))

except Exception as e:
    print("error : ", e)


def inserttosqlrooms(valsarr):
    def sqlconnect(filename='test.db'):
        try:
            con = lite.connect(filename)
            return con
        except lite.Error as e:
            print("Connect To Sql Error :  ", e)

    def sqlcursor(con):
        cur = con.cursor()
        return cur

    con = sqlconnect()
    cur = sqlcursor(con)

    try:
        for roomID in (valsarr.keys()):
            vals = ""
            keys = ["address ", "city ", "company ", "escapecard ", "facebook ", "favicon ", "id ", "link ", "name ",
                    "people ", "review_score ", "roomescape_id  ", "selected  ", "tel  ", "trip"]

            for k in keys:
                val = str(valsarr[roomID][str(k).strip()])
                """ translate to hebrew if needed"""
                if 'u0' in str(val):
                    val = gethebrew(val)

                vals = vals + "\"" + val + "\"" + ","

            __datenow = str(datetime.datetime.now()).split(" ")[0]
            __timenow = str(datetime.datetime.now()).split(" ")[1]
            vals = vals + "\"" + __datenow + "\"" + ","
            vals = vals + "\"" + __timenow + "\"" + ","

            vals = vals.strip(",")
            query = str(
                "INSERT INTO Rooms(address ,city ,company ,escapecard ,facebook ,favicon ,id ,link ,name ,people ,review_score ,roomescape_id  ,selected  ,tel  ,trip ,currDate , currTime) VALUES (" + vals + ")")
            cur.execute(query)


    except Exception as e:
        print(e)

    con.commit()

    if con:
        con.close()


def inserttosqlroomdates(valsarr):
    def sqlconnect(filename='test.db'):
        try:
            con = lite.connect(filename)
            return con
        except lite.Error as e:
            print("Connect To Sql Error :  ", e)

    def sqlcursor(con):
        cur = con.cursor()
        return cur

    def sqlvacum(conn):
        conn.execute("VACUUM")

    con = sqlconnect()
    cur = sqlcursor(con)
    sqlvacum(con)

    try:

        __datenow = str(datetime.datetime.now()).split(" ")[0]
        __timenow = str(datetime.datetime.now()).split(" ")[1]
        daysAhadCounter = 5
        for d in valsarr.keys():  # foreach date
            for k in valsarr[d]:  # foreach room
                vals = ""
                __room = str(k)
                __times = str(valsarr[str(d)][k])
                __roomDate = str(d)

                vals = vals + "\"" + __datenow + "\"" + ","
                vals = vals + "\"" + __timenow + "\"" + ","
                vals = vals + "\"" + __roomDate + "\"" + ","

                vals = vals + "\"" + __room + "\"" + ","
                vals = vals + "\"" + __times.strip(",") + "\"" + ","
                vals = vals.strip(",")
                query = str(
                    "INSERT INTO RoomDates(currDate ,currTime , roomDate ,roomId ,roomTimes) VALUES (" + vals + ")")
                cur.execute(query)
            daysAhadCounter = daysAhadCounter - 1
            if daysAhadCounter == 0:
                break


    except Exception as e:
        print(e)

    con.commit()

    if con:
        con.close()


if __name__ == "__main__":

    """
    roomsJson
    citiesArr
    datesArr
    regionsCitiesArr
    """

    roomsarray = {}
    datesandroomsarray = {}

    start = time.time()

    inserttosqlrooms(roomsJson)

    for d in datesArr.keys():

        for t in datesArr[d]:
            try:
                roomsarray[t[1]]
            except:
                roomsarray[t[1]] = ""

            roomsarray[t[1]] = roomsarray[t[1]] + "," + t[0]

        datesandroomsarray[d] = roomsarray
    inserttosqlroomdates(datesandroomsarray)

    print("finished ", time.time() - start)
