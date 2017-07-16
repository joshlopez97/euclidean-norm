# script uses ctypes to call a C++ function euclidean() to calculate euclidean norm of a
# vector of length N and prints the result to the console (with precision of 16 decimals)
import ctypes
import sys
from decimal import Decimal

if not sys.version_info[0] == 2 or sys.version_info[1] < 7:
	print("Error: Python 2.7.x is required to run this script")
	exit()

# read line of floats into values list
fileName = "c-python.txt"
try:
	with open(fileName) as file:
		for line in file:
			values = map(Decimal, line.split()) # Decimal has more precision than Python float
except IOError:
	print("Error: Unable to read file " + fileName)
	exit()

# calculate length of list
length = len(values)

# cast python list to C++ array
cppValues = (ctypes.c_double * length)(*values)

# access dynamic link library
dll = ctypes.CDLL("euclidean.so")

# set return type to C++ double
dll.euclidean.restype = ctypes.c_double

# print result
result = dll.euclidean(length, cppValues)
print('{0:.16f}'.format(result))