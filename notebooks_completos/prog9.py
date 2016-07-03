import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="Muestra el número que le hayamos pasado elevado al cuadrado")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="incrementa la verbosidad de la salida por pantalla")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print("El número {} elevado al cuadrado es {}".format(args.square, answer))
else:
    print(answer)
