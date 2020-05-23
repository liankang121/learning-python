from multiprocessing import Process

def write_to_new(start,size,f,filename):
    f.seek(start,0)
    print(f.tell())
    data = f.read(size)
    with open(filename,"wb") as new_file:
        new_file.write(data)



with open("8.txt", "ab+") as f:
    size = f.tell()
    print(size)
    f.seek(0,0)
    p = Process(target=write_to_new,args=(0,size//2,f,"b.txt"))
    p2 = Process(target=write_to_new,args=(size//2,size//2,f,"C.txt"))
    p.start()
    p2.start()
    p.join()
    p2.join()


