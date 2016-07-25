#!/usr/bin/env python3

# Probando yield from. Sirve para que un generador delegue en otro

def grep(pattern):
    """
        Esto es una corrutina:
        - Al llamarla, le pasamos como argumento el patron a buscar
        - A partir de ahí, cada vez que le mandemos texto con send() desde fuera, lo recogerá con yield
        - Si el texto que le mandemos contiene el patron, se limitara a imprimir la linea recibida
        Estamos implementado un pipe, vamos
    """
    print("Looking for {}".format(pattern))
    try:
        while True:

            # Recojo lo que me manden
            line = (yield)

            # Si el patrón está en lo que me han mandado, lo imprimo
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("Cerrando")



# Creamos la corrutina
g = grep("python")

# La arrancamos
g.send(None)

# Le mandamos cosas
g.send("Hola")
g.send("Hola")
g.send("Hola")
g.send("python")

# La cerramos
g.close()
