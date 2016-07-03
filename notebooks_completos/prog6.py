import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="incrementa la verbosidad de la salida por pantalla")
args = parser.parse_args()
if args.verbosity:
    print("Ahora saco más cosas por pantalla")
