def square_root(x): #as no library allow use define function
    if x < 0:
        return("Input must be a non-negative integer.")
    elif x == 0 or x == 1:
        return x 

    return int(x ** 0.5) #since can safely assume is a perfect square so we use **.5

perfect_square = 4 #assume is a perfect square
result = square_root(perfect_square)
print(result)

#Bonus
# space-complexity analysis
# O(1) as use a constant amount of space based on the input size
# time-complexity analysis
# O(1) as running the algorithm does not depend the input size as the int(x**.5) is a constant time operation
