import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="simplemente muestra por pantalla la cadena que le pasemos en esta posición")
args = parser.parse_args()
print(args.echo)
