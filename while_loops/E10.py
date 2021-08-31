#!/usr/bin/python

#represent 2 numbers 
#n1_n2: Num , Num -> Num Num
#takes 2 numbers, the program will ask for the second number
#everytime this one is not higher than the first one, the second
#number will be re-asked
#gives the two numbers

def n1_n2():
    n1 = int(input("Enter the first number "))
    n2 = int(input("Enter the second number "))

    while n2 <= n1:
        n2 = int(input("Enter the second number "))

    print (n1, n2)

n1_n2()
    