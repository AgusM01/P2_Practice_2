#!/usr/bin/python

#Represent Fahrenheit grades to Celcius grades by int
#table_farCel: int -> int 
#takes temperatures in fahrenheit
#gives the convertion to celcius on a table
#input: (none) , output: Fahrenheit:40 Celcius:4.444
#                        Fahrenheit:60 Celcius:15.555
#                        Fahrenheit:0 Celcius:-17.777

def farCel(f):
     return (f-32)*5/9

def table_farCel():
    
    for i in range(10,130,10):
        print("Fahrenheit:",i , "Celcius:", farCel(i))


table_farCel()

