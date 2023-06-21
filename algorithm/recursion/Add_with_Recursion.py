### Implement a custom add function given an increment and a decrement function:

def inc(x) :
    """Increments and returns the given integer."""
    if not isinstance(x, int):
        raise TypeError("Given number is not an integer.")
    return x + 1


def dec(x) :
    """Decrements and returns the given integer."""
    if not isinstance(x, int):
        raise TypeError("Given number is not an integer.")
    return x - 1


def add(x, y):
    """Adds and returns two given integers with increment and decrement functions."""
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Given input is not an integer.")
    if x < 0 or y < 0:
        raise ValueError("One or more inputs are less than 0.")
    
    # Implement your code here.
    ## need to call inc function of x for y times (or the opposite)
    sum = x # sum starts from value of x
    for i in range (0, y): #inc is called for y times
        sum = inc(sum) # each time sum increments by 1

    return sum # add function returns the final sum

input_x = int(input("Enter the first number you wish to add: ")) # input the x for adding
input_y = int(input("Enter the second number you wish to add: "))# input the y for adding
print("the addition of "+str(input_x)+" and "+str(input_y)+" is: "+str(add(input_x, input_y)) )