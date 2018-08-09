#!/usr/bin/python

from multiprocessing import Process, Manager, Value, Lock, Pool
import time

NUM = Value('i', 0)
lock = Lock() 

def Oadd():
    global NUM, lock
    with lock: 
        NUM.value += 1
        print NUM.value
        print "-----------------"
    
if __name__ == '__main__':
    t_start=time.time()
    elenum = Value('i', 0)
    pool = Pool(10)  
    for i in range(800):
        pool.apply_async(Oadd)
    pool.close() 
    pool.join()
    pool.terminate()
    t_end=time.time()
    t=t_end-t_start
    print 'the program time is :%s' %t
