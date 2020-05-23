from threading import *
from time import *

s = None
e = Event()


def yangzilong():
    print("天王盖地虎")
    global  s
    s = "宝塔镇河妖"
    e.set()


t = Thread(target=yangzilong())
t.start()
e.wait()
if s == "宝塔镇河妖":
    print("自己人")
    print("querenguo yashen ")
else:
    print("dasi ")
t.join()
