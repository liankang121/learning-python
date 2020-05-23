import  threading
from time import *
import os

a = 100

def func():
    for i in range(3):
        print("播放：adfdf")
        sleep(2)
        global a
        a = 100
        print(a)

t1 = threading.Thread(target=func)
t1.start()
for i in range(2):
    sleep(1)
    print("s")
print("a:",a)
t1.join()