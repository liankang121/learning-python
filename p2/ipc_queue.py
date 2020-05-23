from multiprocessing import  Queue,Process
from time import  *
from random import randint

q = Queue(5)

def get_number():
    for i in range(6):
        num = randint(1,22)
        q.put(num)
    q.put(randint(1,15))

def num_requset():
    while True:
        sleep(3)
        try:
            data = q.get(timeout=3)
        except:
            break
        print(data, end="") #长时间没有打印出来，是因为print内部有会有缓存

p1 = Process(target=get_number)
p2 = Process(target=num_requset)
p1.start()
p2.start()
p1.join()
p2.join()