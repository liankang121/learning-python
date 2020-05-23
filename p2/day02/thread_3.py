from threading import *

from time import *

def func():
    for i in range(2):
        print("hello")

t = Thread(target=func)
print(t.name)
print(t.setName("t1"))
print(t.getName())
t.start()
print("t.is_alive:",t.is_alive())
t.join()