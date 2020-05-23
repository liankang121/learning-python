import  multiprocessing as mp
from time import  *

def func():
    print("这是一个子进程")
    sleep(4)
    print("子进程执行完毕")

def main_func():
    print("这是一个付进程")
    sleep(2)
    print("父进程执行完毕")

p = mp.Process(target=func)
p.start()
main_func()
p.join()

