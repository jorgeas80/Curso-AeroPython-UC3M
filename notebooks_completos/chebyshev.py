import argparse
import numpy

# Build a basic parser.
help_text = '''Crea gráfica de polinomios de Chebysev de órdenes M a N para valores entre -X y +X.'''
sign_off = 'Author: Bob Dowling <rjd4@cam.ac.uk>'

parser = argparse.ArgumentParser(description=help_text, epilog=sign_off)

# Add the command line options
parser.add_argument('-k', '--npts',  dest='npts',  type=int,   default=512, metavar='k', help='Número de puntos a graficar')
parser.add_argument('-x', '--limit', dest='limit', type=float, default=1.0, metavar='X', help='Rango de valores para x.')
parser.add_argument('-m', '--min',   dest='min',   type=int,   default=1,   metavar='m', help='Orden mínimo del polinomio.')
parser.add_argument('-M', '--max',   dest='max',   type=int,   default=3,   metavar='M', help='Orden maximo del polinomio.')
parser.add_argument('-t', '--title', dest='title', type=str,   default='',  metavar='title', help='Título de la gráfica')
parser.add_argument(                 dest='file',  type=argparse.FileType('wb'),  metavar='fname', help='Nombre del fichero para guardar la gráfica (obligatorio)')

# Parse the command line
arguments = parser.parse_args()
# print(arguments)

# Create the graph
# Matplotlib is slow to load so put it here to not delay the parsing
import matplotlib.pyplot as pyplot

npts = arguments.npts
limit = arguments.limit
x = numpy.linspace(-1.0*limit, limit, npts)

# Run through the Chebyshev polynomials
M = arguments.min
N = arguments.max + 1
for order in range(M,N):
    y = numpy.where(
        numpy.abs(x) < 1.0,
        numpy.cos(order*numpy.arccos(x)),
        numpy.where(
            x > 0.0,
            numpy.cosh(order*numpy.arccosh(x)),
            (-1.0)**order*numpy.cosh(order*numpy.arccosh(numpy.abs(x)))
            )
        )

    pyplot.plot(x,y)

if arguments.title:
    pyplot.suptitle(arguments.title)

f = arguments.file
pyplot.savefig(f)
f.close()

