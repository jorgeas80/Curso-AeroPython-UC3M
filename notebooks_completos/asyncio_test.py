#!/usr/bin/env python3
"""
    Ejemplo de uso de asyncio: nos permite implementar concurrencia en un solo hilo de ejecución,
    implementando un bucle de eventos que le va danto turnos a diferentes tareas. Una tarea puede
    detenerse mediante una llamada a yield from. En ese momento, el bucle de eventos le da turno
    a la siguiente tarea
"""
import asyncio

# Con este decorador, marcamos la función como una corrutina utilizable
# por asyncio. Es decir, puede llamar a otras corrutinas con yield from, y ser llamada
# por otras mediante el mismo mecanismo.
@asyncio.coroutine
def snooze(i):
    print("Corrutina {} durmiendo 5 segundos".format(i))

    # En este punto, snooze para durante 5 segundos, hasta que asyncio.sleep vuelve.
    # Si la corrutina devolviera un valor, lo podríamos guardar, pero en este caso simplemente
    # se duerme durante X segundos. Simula el comportamiento de una operación I/O no bloqueante,
    # porque en ese segundo que pasa, el bucle de eventos le puede dar el turno a otra tarea
    yield from asyncio.sleep(5)
    print("Corrutina {} despierta".format(i))

def main():

    loop = asyncio.get_event_loop()
    tasks = []

    for i in range(10):

        # Metemos la tarea en una estructura de datos que nos asegura que se va a mantener viva hasta que la tarea se complete
        # Podría compararse a una promesa en JavaScript
        task = asyncio.ensure_future(snooze(i))
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == "__main__":
    main()
