#!/usr/bin/env python3

"""
    Esto es básicamente azucar sintáctico sobre asyncio
"""
import asyncio

# Ya no hace falta decorar la función para hacerla una corrutina válida.
# Basta con definirla como async
async def snooze(i):
    print("Corrutina {} durmiendo 5 segundos".format(i))

    # En vez de yield from hacemos await, que es más expresivo. No son exactamente
    # lo mismo, pero la diferencia es sutil. Se explica aquí http://www.snarky.ca/how-the-heck-does-async-await-work-in-python-3-5
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
