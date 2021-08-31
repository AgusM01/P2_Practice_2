#!/usr/bin/python

#Calculate the final value of a debt including interests
#final_debt: int, float, int -> float
#takes quantity in argentine pesos
#takes interest rate
#takes quantity of years
#gives the final mount of a debt including interests
# input:  100, 20%, 5 ; output: 101.004008
# input:  10000, 70%, 10 ; output: 10722.4668
# input:  300, 0.5%, 30 ; output: 304.5327778

def final_debt():
    c = int(input("Enter the initial amount in pesos "))
    x = float(input("Enter the interest rate "))
    n = int(input("Enter the quantity of years "))
    f = 1
    for i in range (1, n + 1):
        f = (1 + x/100) * f 
    print (c * f)


final_debt()


