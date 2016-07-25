def printer():
    """
        Corrutina que simplemente recibe datos y los escupe
    """
    print("Preparing to print...")
    try:
        while True:
            line = (yield)
            print(line)
    except GeneratorExit:
        print("Cerrando printer")


def grep(pattern, consumer):
    """
        Corrutina que filtra datos y se los manda a otra corrutina
    """
    print("Looking for {}".format(pattern))

    try:
        while True:
            s = (yield)
            if pattern in s:
                consumer.send(s)
    except GeneratorExit:
        print("Cerrando grep")
        consumer.close()



# Creamos la corrutina final y la arrancamos
p = printer()
p.send(None)

# Creamos la corrutina que filtra y la arrancamos
g = grep("ending", p)
g.send(None)

# Este es el texto que metemos en nuestra cadena de corrutinas
text = 'Commending spending is offending to people pending lending!'

# Vamos mandando texto a la corrutina principal
for line in text.split():
    g.send(line)


#  Y cerramos
g.close()

