#!/usr/bin/python

#decides wherever a number is prime or not
#is_prime: number -> boolean
#takes a number
#gives true if this one is true, or false if it is false
#input: 2 ; output: True
#input: 4 ; output: False
#input: 5 ; output: True

def is_prime(x):
    n = 0
    i = 1
    while i != x:
        if (i == 1): #1 is divisor of all numbers but is not a prime 
            i = i + 1 
        elif (x % i) == 0:
            n = n + 1
            i = i + 1
        else:
            i = i + 1
    if n > 1:
        return False
    else:                
        return True


#represent all the prime numbers up to a n-value
#primes: number -> numbers
#takes a number n
#gives all the prime numbers up to n
#input: 7 ; ouyput: 2, 3, 5 ,7
#input: 13 ; ouyput: 2, 3, 5 , 7, 11, 13
#input: 1 ; ouyput: 0

def primes():
    n = int(input("Enter the number "))
    i = 2 
    while i != n :
        if is_prime(i):
            print (i)
        i = i + 1

primes()

    