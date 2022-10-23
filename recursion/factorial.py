### code that calculate & prints factorial of an interger number

def calculate_factorial(n): # function that calculates factorial
    if n<0: # factorial of a negative value does not exist, print undefined
        return "undefined" 
    elif n == 0 or n == 1: # both factorial of 0 and factorial of1 is 1
        return 1 
    else: # re-enter the calculate_factorial function until the number reaches 1, the multiplication will be accumulated
        return n*calculate_factorial(n-1) 
    
# enter the input number you wish to calculate, should be an integer
input_num = int(input("Enter the number you wish to calculate factorial of: "))

# print out the calculated factorial of the input
print("Factorial of the input number is "+str(calculate_factorial(input_num)))