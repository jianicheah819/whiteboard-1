def max_char_occurence(input_str):
    #remove whitespace and punctuation
    newstring = ''.join(char for char in input_str if char.isalnum())

    # Create a dictionary to store character counts
    count_char = {}
    for char in newstring:
        if char in count_char:
            count_char[char] += 1 #to check each element and if already got same char in dict then add one 
        else:
            count_char[char] = 1

    max_char = max(count_char, key=count_char.get) #to find the key that have max value that return the alphabet
    max_occurrence = count_char[max_char] #to access the value of key assign to max_char

    return {'Character': max_char, 'Occurrence': max_occurrence}

# Get user input for the string
user_input = input("Enter a string: ")
result = max_char_occurence(user_input)
print(result)

#Bonus
# By using isalnum() where return True means are mix letters and number and return False if not.
# By using this we can works with different language as well. 