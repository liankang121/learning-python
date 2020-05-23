from multiprocessing import Value,Process
from time import  *
from random import  randint

money = Value("i",5000)
def man():
    for i in  range(30):
        sleep(0.14)
        money.value += randint(1,1000)

def girl():
    for i in range(30):
        sleep(0.1)
        money.value -= randint(200,800)

p1 = Process(target=man)
p2 = Process(target=girl)
p1.start()
p2.start()
p1.join()
p2.join()
print(money)



