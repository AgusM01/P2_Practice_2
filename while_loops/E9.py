#!/usr/bin/python

#shows the final average on a float
#average: n-float -> float
#takes a n-number of grades
#gives the final average of the marks
#input: 3, 4, 7 ; output: 4.6666
#input: 2.50, 7.80, 4.40 ; output: 4.9
#input: 6.70, 8.30, 9.10 ; output: 8.033333

def average():
    ans = "yes"
    f = 0 
    x = 0 
    while ans == "yes":
        n = int(input ("Enter the grade "))
        f = n + f
        x = x + 1
        ans = input("Would you like to enter another mark? yes / no ")

    print ("The average is: ", f/x)

average()



