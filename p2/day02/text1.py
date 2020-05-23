from time import *
from threading import *
from multiprocessing import *


def test_running_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time() - start_time
        print(end_time)
        return func(*args, **kwargs)

    return wrapper


# @test_running_time
def count():
    c, x, y = 0, 0, 0
    while c < 1800000:
        c += 1
        x += 1
        y += 1


def write_text():
    f = open("text", 'w')
    for i in range(1800000):
        f.write("hello\n")
    f.close()


def read_text():
    f = open("text", "r")
    linns = f.readlines()
    f.close()


def IO_1():
    write_text()
    read_text()


start_time = time()
for i in range(10):
    count()
end_time = time() - start_time
print(end_time)

start_time = time()
jobs = []
for i in range(10):
    P1 = Process(target=count)
    jobs.append(P1)
    P1.start()

for item in jobs:
    item.join()
end_time = time() - start_time
print(end_time)

start_time = time()
tjobs = []
for i in range(10):
    t = Thread(target=count)
    tjobs.append(t)
    t.start()
for item in tjobs:
    item.join()
end_time = time() - start_time
print(end_time)


print("----------------------")
start_time = time()
for i in range(10):
    IO_1()
end_time = time() - start_time
print(end_time)

start_time = time()
jobs = []
for i in range(10):
    P1 = Process(target=IO_1)
    jobs.append(P1)
    P1.start()

for item in jobs:
    item.join()
end_time = time() - start_time
print(end_time)

start_time = time()
tjobs = []
for i in range(10):
    t = Thread(target=IO_1)
    tjobs.append(t)
    t.start()
for item in tjobs:
    item.join()
end_time = time() - start_time
print(end_time)