import threading

def countdown(n):
    while n > 0:
        n -= 1

COUNTDOWN = 100000000 # 100 MILLONES
t1 = threading.Thread(target=countdown,args=(COUNTDOWN//2,))
t2 = threading.Thread(target=countdown,args=(COUNTDOWN//2,))
t1.start(); t2.start()
t1.join(); t2.join()
