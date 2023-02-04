#Practice Python: Find prime number 
import string, itertools

class Optimus_Prime:
    @classmethod
    def user_prime_check(cls) -> None:
        while True:
            u_input = input("Input number to check: ")
            try:
                cls.cls.i_input = int(u_input)
            except: 
                print("Please input a number.\n")    
            if cls.i_input == 0:
                print("The number is zero number.\n")
                continue
            elif cls.i_input == 2 or cls.i_input == 3: #list(range(1,4,1)) does not work-why?
                print("The number is a prime number.\n")
                continue
            elif (cls.i_input % 2) == 0 or (cls.i_input % 5) == 0:
                print("The number is not a prime number.\n")
                continue
            elif (cls.i_input % 3) != 0:
                print("The number is a prime number.\n")
                continue
            else:
                raise Exception("Sassfrass.")

    @classmethod
    def prime_check(cls) -> None:   
        u_input = input("Input number to check: ")
        cls.i_input = int(u_input)
        if u_input == 0:
            print("The number is zero number.\n")
        elif cls.i_input == 2:
            print("The number is a prime number.\n")
        elif (cls.i_input % 2) == 0 or (cls.i_input % 5) == 0:
            print("The number is not a prime number.\n")
        elif (cls.i_input % 3) != 0:
            print("The number is a prime number.\n")
        elif u_input.isdigit() == "false":
            print("Please input a number.\n")  
        else:
            raise Exception("Danger, Will Robinson.")
            SystemExit
    
optimus_prime = Optimus_Prime
optimus_prime.user_prime_check()
# optimus_prime.prime_check()


