from datetime import datetime

nowTime = (datetime.now().strftime('%H:%M'))
someTime = ('18:50')

s1 = someTime.split(':')
s2 = nowTime.split(':')

if s1[0] == s2[0]:
    print(int(s1[1]) - int(s2[1]) <=10)

    print(nowTime)
