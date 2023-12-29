def generate_fibonacci(n):
    if n <= 0:
        return [] #if the number of fib seq is 0 then return empty list
    elif n == 1:
        return [0] #if the number of fib seq is 1 then return 0 in the list
    elif n == 2:
        return [0, 1] #if the number of fib seq to generate is 2 then return 0 and 1 in the list
    else: #if greater than 2
        fib_sequence = generate_fibonacci(n - 1) #call the function itself to break the number to generate the fib seq element one by one 
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) #with the formula F(n-1)+F(n-2)
        return fib_sequence
    
# Get user input for the number of Fibonacci sequence elements
n = int(input("Enter the number of Fibonacci sequence elements to generate: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = generate_fibonacci(n)
    print(result)


