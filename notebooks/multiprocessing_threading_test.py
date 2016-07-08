#!/usr/bin/env python3

from threading import Thread
from multiprocessing import Process
from time import sleep

def snooze(i):
    print("Hilo {} durmiendo 5 segundos".format(i))
    sleep(5)
    print("Hilo {} despierto".format(i))

def thread_snooze():
    threads = []

    for i in range(5):
        thread = Thread(target=snooze, args=(i, ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def main():
    processes = []

    for i in range(2):
        process = Process(target=thread_snooze)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
