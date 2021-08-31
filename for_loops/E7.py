#!/usr/bin/python

#shows the first n triangular numbers
#triangular: int -> int
#take a number n
#gives all triangulars numbers form 1 to n
#input: 2 ; output: 1 1-1
#                   2 2-3
#input: 3 ; output: 1 1-1
#                   2 2-3
#                   3 3-6
#input: 0 ; output: error

def triangular():
    n = int(input("Enter your n number "))

    if n < 1:
        print("error")
    else:
        tri = 0
        for i in range (1 , n + 1):
            tri = tri + i

            print(i,"_", i, "-", tri)

triangular()

#shows the first n triangular numbers using the formal ecuation
#triangular_ecu: int -> int
#take a number n
#gives all triangulars numbers form 1 to n
#input: 2 ; output: 1 1-1
#                   2 2-3
#input: 3 ; output: 1 1-1
#                   2 2-3
#                   3 3-6
#input: 0 ; output: error

def triangular_ecu():
    n = int(input("Enter your n number "))

    if n < 1:
        print("error")
    else:
        tri = 0
        for i in range (1 , n + 1):
            tri = ((i * (i + 1))/2)

            print(i,"_", i, "-", tri)

triangular_ecu()
