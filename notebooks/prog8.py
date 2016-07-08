import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", "-v", help="incrementa la verbosidad de la salida por pantalla", action="store_true")
args = parser.parse_args()
if args.verbose:
    print("Ahora saco más cosas por pantalla")
