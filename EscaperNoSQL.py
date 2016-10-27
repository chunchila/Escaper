from pymongo import MongoClient
from datetime import datetime

arrHours = [["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"],
            ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"],
            ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"],
            ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"],
            ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"],
            ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["19:00"],
            ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"],
            ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"],
            ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["15:00"], ["16:00"], ["17:00"],
            ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"],
            ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"],
            ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"],
            ["16:00"], ["17:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"],
            ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"],
            ["21:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"],
            ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"],
            ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"],
            ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"],
            ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"],
            ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["14:00"], ["15:00"], ["16:00"],
            ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"],
            ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"],
            ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"],
            ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"],
            ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"],
            ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"],
            ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"],
            ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"],
            ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"],
            ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"],
            ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"],
            ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"],
            ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"],
            ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"],
            ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"],
            ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"],
            ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"],
            ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"],
            ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"],
            ["12:00"], ["13:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"],
            ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"],
            ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"],
            ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"],
            ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"],
            ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"],
            ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"],
            ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"],
            ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"],
            ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"],
            ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"],
            ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"],
            ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"],
            ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"],
            ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"],
            ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"],
            ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"],
            ["18:00"], ["19:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"],
            ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"],
            ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"],
            ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"],
            ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"],
            ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"],
            ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"],
            ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"],
            ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"],
            ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"],
            ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["12:00"], ["13:00"], ["14:00"],
            ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"],
            ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"],
            ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"],
            ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"],
            ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["18:00"],
            ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"],
            ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"],
            ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"],
            ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"],
            ["10:00"], ["11:00"], ["12:00"], ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"],
            ["19:00"], ["20:00"], ["21:00"], ["22:00"], ["23:00"], ["00:00"], ["10:00"], ["11:00"], ["12:00"],
            ["13:00"], ["14:00"], ["15:00"], ["16:00"], ["17:00"], ["18:00"], ["19:00"], ["20:00"], ["21:00"],
            ["22:00"], ["23:00"], ["00:00"]]
post = {
    "address": {
        "street": "2 Avenue",
        "zipcode": "10075",
        "building": "1480",
        "coord": [-73.9557413, 40.7720266]
    },
    "borough": "Manhattan",
    "cuisine": "Italian",
    "hours": arrHours,
    "name": "Vella"
}
import time
for x in range(10):
    with MongoClient('localhost', 27017) as client:
        db = client.test_database
        col = db.restaurants
        col.insert(post)

    for x in col.find():
        print(x)
    print(db.restaurants.count())
