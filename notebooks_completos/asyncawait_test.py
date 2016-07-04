#!/usr/bin/env python3

import asyncio

async def snooze(i):
    print("Corrutina {} durmiendo 5 segundos".format(i))
    await asyncio.sleep(5)
    print("Corrutina {} despierta".format(i))


def main():

    loop = asyncio.get_event_loop()
    tasks = []

    for i in range(10):
        task = snooze(i)
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == "__main__":
    main()
