#Determine nth Fibonacci's number

def N_thFib(n):
    if n < 0: # fibonacci starts from index 0
        return "undefined"
    elif n == 0: #value of 0th fibonacci sequence is 0
        return 0
    elif n == 1: #value of 1th fibonacci sequence is 1
        return 1
    else: # from the first two elements of fibonacci sequence, calculate proceeding ones, which are additions of n-1 th and n-2 th element
        return N_thFib(n-1) + N_thFib(n-2)

input_num = int(input("Enter the number you wish to : ")) #enter the number
print("the "+str(input_num)+"th Fibonacci number is: "+str(N_thFib(input_num))) #print the nth fibonacci number