from datetime import datetime
import os

def calcDiffMin(time, diff=10):
    nowTime = (datetime.now().strftime('%H:%M'))
    someTime = (str(time))

    s1 = someTime.split(':')
    s2 = nowTime.split(':')

    if s1[0] == s2[0]:
        if (int(s1[1]) - int(s2[1]) <= diff):
            return (int(s1[1]) - int(s2[1]))
        else:
            return None


if __name__ == "__main__":
    print("im in main ")

    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    print(arr[1:6:6])
    for x in range(100):
        print("moshe for x ", x, x - 1 , x-2)


    if (calcDiffMin("20:20", 10)):
        print('yes')
    else:
        print('no')
