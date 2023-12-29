for i in range(1, 101): #for number 1-100
#conditions to meet
    if i % 3 == 0 and i % 5 == 0: 
        print("FizzBuzz", end=' ') #end='' is to make sure it print in one line with space
    elif i % 3 == 0: #'%' is the remainder. If divide 3 remainder is 0 means can divide by 3
        print("Fizz", end=' ')
    elif i % 5 == 0:
        print("Buzz", end=' ')
    else:
        print(i, end=' ') #if none of the conditions met, then will print the number. 