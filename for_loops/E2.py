#!/usr/bin/python

#shows on screen all the numbers of de dominó game by integrers
#domino: none -> string
#takes nothing
#gives all the numbers of a dominó piece
#input: (none); output: 0 0, 0 1, 0 2, ..., 6 6

def domino():
    n = 0
    for n in range (0 , 7):
        for i in range (1 , 7):
            print (n, i)

        
domino()
