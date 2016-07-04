#!/usr/bin/env python3

from threading import Thread
from time import sleep

def snooze(i):
    print("Hilo {} durmiendo 5 segundos".format(i))
    sleep(5)
    print("Hilo {} despierto".format(i))

def main():
    threads = []

    for i in range(10):
        thread = Thread(target=snooze, args=(i, ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
