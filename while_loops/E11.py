#!/usr/bin/python

#represent the number of multiples of a number n1 lower than
#a number n2 
#multiples_n: num , num --> num
#takes a number n1 and a number n2
#return the quantity of multiples of n1 lower than n2
# input: 4, 20 ; output: 5
# input: 7, 30 ; output: 5
# input: 5, 50 ; output: 10

#using for loop

def multiples_n_for():
    n1 = int(input("Enter the first number "))
    n2 = int(input("Enter the second number "))
    x = 0
    for i in range (n1, n2 + 1):
        multiple = n1 * i

        if multiple < n2:
            x = x + 1
    
    print ("There are", x, "multiples of", n1 ,", higher than", n1, "and lower than", n2)


#multiples_n_for()

#using while loop

def multiples_n_while():
    n1 = int(input("Enter the first number "))
    n2 = int(input("Enter the second number "))
    x = 0
    multiple = 0
    
    while multiple < n2:
        
        x = x + 1 #Counting zero in first sum  
        multiple = n1 * x
        
        
    
    print ("There are", x, "multiples of", n1 , "lower than", n2)

#multiples_n_while()

#The while_loop is clearer and it works with less operations  