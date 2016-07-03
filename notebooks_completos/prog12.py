import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="la base")
parser.add_argument("y", type=int, help="el exponente")
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.x**args.y
if args.verbosity >= 2:
    print("Ejecutando '{}'".format(__file__))
if args.verbosity >= 1:
    print("{}^{} == ".format(args.x, args.y), end="")
print(answer)
