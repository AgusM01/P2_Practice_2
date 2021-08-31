#!/usr/bin/python

#decides whereas a number is a power of two 
#is_power_of_two: Num -> Boolean
#takes a number
#gives true if the number is a power of two, false if not
#input: 2 ; output: true
#input: 32 ; output: true
#input: 3 ; output: false

def is_power_of_two(x):
    n = 0
    k = 0
    while n != x:
        if pow(2, n) == x:
            n = x
            k = 1
            return True
        else:
            n = n + 1
    if k == 0:
        return False

#if is_power_of_two(64):
    print("AA")

#returns the sum of all power of two in a range of two numbers
#pow_2_sum: Num Num -> Num
#takes two numbers
#gives the sum of all the power of two between those two numbers
#input: 0, 9; output: 15
#input: 2, 10; output: 14
#input: 5, 6; output: 0

def pow_2_sum():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: ")) 
    p = 0
    i = n1
    while i != n2:
        if is_power_of_two(i):
            p = i + p
            i = i + 1         
        else:
            i = i + 1
            
    print(p)

pow_2_sum()

    

