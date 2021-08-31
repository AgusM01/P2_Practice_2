#!/usr/bin/python

#calculate the factorial of a m quantity of numbers 
#m_factorial: int, m-ints -> m-ints
#takes a number m which indicates the quantity of numbers
#to enter, and the number itself
#gives the factorial of each number entered
#input: 3 , 4, 5, 6 ; output: 24, 120, 720
#input: 2 , 1, 8 ; output: 1, 40320
#input: 1 ,0 ; output: 1

m = int(input("Enter the quantity of numbers m "))

def m_factorial(m):
    for i in range (1, m + 1):
        
        factorial = 1
        
        n = int (input ("Enter the number to do the factorial "))
    
        for a in range(1, n + 1):
            
            factorial = factorial * a
    
        print (factorial)

m_factorial(m)


