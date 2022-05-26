#Practice Python: Find prime number 
import string, itertools


def user_prime_check():
    while True:
        u_input = input("Input number to check: ")
        try:
            i_input = int(u_input)
        except: 
            print("Please input a number.\n")    
        if i_input == 0:
            print("The number is zero number.\n")
        elif i_input == 2 or i_input == 3: #list(range(1,4,1)) does not work-why
            print("The number is a prime number.\n")
            continue
        elif (i_input % 2) == 0 or (i_input % 5) == 0:
            print("The number is not a prime number.\n")
            continue
        elif (i_input % 3) != 0:
            print("The number is a prime number.\n")
            continue
        else:
            raise Exception("Danger Will Robinson.")


def prime_check():   
    u_input = input("Input number to check: ")
    i_input = int(u_input)
    if u_input == 0:
        print("The number is zero number.\n")
    elif i_input == 2:
        print("The number is a prime number.\n")
    elif (i_input % 2) == 0 or (i_input % 5) == 0:
        print("The number is not a prime number.\n")
    elif (i_input % 3) != 0:
        print("The number is a prime number.\n")
    elif u_input.isdigit() == "false":
        print("Please input a number.\n")  
    else:
        raise Exception("Danger Will Robinson.")
        SystemExit
    

user_prime_check()


