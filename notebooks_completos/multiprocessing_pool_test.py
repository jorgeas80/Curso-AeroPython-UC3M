#!/usr/bin/env python3

from multiprocessing import Pool
from time import sleep

def snooze(i):
    print("Proceso {} durmiendo 5 segundos".format(i))
    sleep(5)
    print("Proceso {} despierto".format(i))

def main():
    pool = Pool(processes=2) # numero de cpus
    results = []

    for i in range(10):
        result = pool.apply_async(snooze, (i, ))
        results.append(result)

    for result in results:
        result.get()

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
