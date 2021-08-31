#!/usr/bin/python

#verify the enter of a positive number
#is_positive: any -> str
#takes any value
#gives a pass-str in case the value is a positive number.
#if not, return a error-str and ask for re-enter value
#input: 3 ; output: is positive
#input: -3 ; output: error , re-enter value
#input: True ; output: error, re-enter value
#input: "Hello" ; output: error , re-enter value

def is_positive():
    n = int (input ("Enter a number "))

    while n <= 0:
        print("Error, please enter a positive number ")
        n = int (input ("Enter a number "))

    return n 

is_positive()
     