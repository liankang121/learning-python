from threading import *
from time import *


class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs={}):
        super().__init__()
        self._target = target
        self._args = args
        self._kwargs = kwargs


def run(self):
    self._target(*self._args, **self._kwargs)

def player(sec, song):
    for i in range(sec):
        print("song:", song)
        sleep(3)


t = MyThread(target=player, args=(2,), kwargs={"song": "hello"})
t.start()
t.join()
