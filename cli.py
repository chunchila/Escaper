from datetime import datetime


def calcDiffMin(time, diff=10):
    nowTime = (datetime.now().strftime('%H:%M'))
    someTime = (str(time))

    s1 = someTime.split(':')
    s2 = nowTime.split(':')

    if s1[0] == s2[0]:
        if(int(s1[1]) - int(s2[1]) <= diff):
            return (int(s1[1]) - int(s2[1]))
        else:
            return None


if (1 ):#calcDiffMin("20:20",10)):
    print ('yes')
else:
    print('no')



for x in range(10,100):
    print (x * x +1*2)



s3 = " moshe is the man "


def makeBlank(times):
    blank =  "*" * times
    return blank



print (makeBlank(10 ) + s3.title() + makeBlank(10))