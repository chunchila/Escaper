import urllib
import threading
import time
import requests


def pinger_urllib(host):
    """
    helper function timing the retrival of index.html
    TODO: should there be a 1MB bogus file?
    """
    t1 = time.time()

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    try:
        req = requests.get(host, headers=headers)
    except:
        pass
    return (time.time() - t1) * 1000.0


def task(m):
    """
    the actual task
    """
    delay = float(pinger_urllib(m))
    print('%-30s %5.0f [ms]' % (m, delay))


# parallelization
tasks = []
URLs = ['http://www.facebook.com', 'http://wikipedia.org']

with open("sitesT.txt") as f:
    txt = f.read()
URLs = txt.split("\n")
semaphore = threading.BoundedSemaphore(10)
for m in URLs:
    semaphore.acquire()
    t = threading.Thread(target=task, args=(m,))
    t.start()
    tasks.append(t)
    semaphore.release()

# synchronization point
for t in tasks:
    t.join()
