import multiprocessing
from time import sleep


class MiClase(object):

    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print('Estoy en el proceso {} y me pasan estos datos: {}'.format(proc_name, self.name))
        sleep(5)
        print('Ya he acabado')


def worker(q):
    obj = q.get()
    obj.do_something()


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()


    queue.put(MiClase('Cacahuete'))

    # Cerramos la cola y esperamos al hilo de background, asegurándonos de que los datos se han flusheado
    queue.close()
    queue.join_thread()

    # Esperamos a que termine el proceso
    p.join()
