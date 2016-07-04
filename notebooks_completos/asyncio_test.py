#!/usr/bin/env python3

import asyncio

@asyncio.coroutine
def snooze(i):
    print("Corrutina {} durmiendo 5 segundos".format(i))
    yield from asyncio.sleep(5)
    print("Corrutina {} despierta".format(i))

def main():

    loop = asyncio.get_event_loop()
    tasks = []

    for i in range(10):
        task = asyncio.ensure_future(snooze(i))
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == "__main__":
    main()
