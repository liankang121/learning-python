from threading import *
from time import *


def func(sec, name):
    for i in range(sec):
        print(sec)
        sleep(3)
        print(name)

jobs = []
for i in range(3):
    t = Thread(target=func, args=(3,), kwargs={"name": "bob"})
    jobs.append(t)
    t.start()

for job in jobs:
    job.join()
