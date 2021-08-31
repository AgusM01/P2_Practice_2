#!/usr/bin/python

#shows on screen all the n numbers of a game by integrers
#game_e3: none -> string
#takes nothing
#gives all the n numbers of a game like dominó 
#input: (none); output: 0 0, 0 1, 0 2, ..., n n

def game_e3():
    n = int(input("Enter the n number "))
    a = 0
    for a in range (0 , n + 1):
        for i in range (1 , n + 1):
            print (a, i)

game_e3()
