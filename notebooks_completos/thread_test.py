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
        # Definimos args así para que lo detecte como tupla. Si pusieramos args=(i) lo cogeria como entero
        thread = Thread(target=snooze, args=(i, ))

        # Esto invoca a run
        thread.start()


        threads.append(thread)

    for thread in threads:

        # Esperamos a que terminen los hilos
        thread.join()

if __name__ == "__main__":
    main()
