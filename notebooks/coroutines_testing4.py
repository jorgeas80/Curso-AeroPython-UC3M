import asyncio
import aiohttp
import json

@asyncio.coroutine
def fetch_page(url, client):
    response = yield from client.get(url)
    assert response.status == 200
    content = yield from response.text()
    print('URL: {0}:  Content: {1}'.format(url, json.loads(content)))


def main():

    # Creamos el bucle de eventos y lo usamos para crear el cliente de sesion HTTP
    loop = asyncio.get_event_loop()
    client = aiohttp.ClientSession(loop=loop)

    # Tareas a ejecutar
    tasks = [
        asyncio.ensure_future(fetch_page('http://jsonplaceholder.typicode.com/posts/1', client)),
        asyncio.ensure_future(fetch_page('http://jsonplaceholder.typicode.com/posts/2', client)),
        asyncio.ensure_future(fetch_page('http://jsonplaceholder.typicode.com/posts/3', client))]

    # Ejecuta el bucle de eventos hasta que termine
    loop.run_until_complete(asyncio.wait(tasks))

    # Cierra recursos
    loop.close()
    client.close()


if __name__ == "__main__":
    main()
