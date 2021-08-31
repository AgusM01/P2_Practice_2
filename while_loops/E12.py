#!/usr/bin/python

#continue with a pre-setted password
#password: string ->  string
#takes a string 
#continue if the password fit returning True or gives an error message and 
#returns False
#password: computer
#input: "science"; output: "wrong password", False
#input: "agus"; output: "wrong password", False
#input: "computer"; output: "correct password", True

def password ():
    p = "computer"
    u = input("Enter the password... ")
    x = 0
    while p != u :
        print("Wrong password. ")
        x = x + 1

        if x <= 5:
            u = input("Enter the password... ") 
        else:
            print ("You've reached the maximun amount of tries ")
            return False

    print("Correct password. ")
    return True       


password()
