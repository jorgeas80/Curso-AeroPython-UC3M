#!/usr/bin/env python3

from multiprocessing import Process
from time import sleep

def snooze(i):
    print("Proceso {} durmiendo 5 segundos".format(i))
    sleep(5)
    print("Proceso {} despierto".format(i))

def main():
    processes = []

    for i in range(10):
        process = Process(target=snooze, args=(i, ))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
