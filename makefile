run: euclidean.o
	python euclidean-norm.py
euclidean.o:
	g++ -Wall -Wextra -O -ansi -pedantic -shared euclidean.cpp -o euclidean.so