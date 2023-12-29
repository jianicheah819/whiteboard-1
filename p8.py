def anagrams_checker(str1, str2):
    str1=str1.lower() #to ignore case sensitiviy 
    str2=str2.lower()

    if (len(str1) == len(str2)):
        sorted_str1 = sorted(str1) #to sort the string and if they are the same, then we can quickly get the answer 
        sorted_str2= sorted(str2)

    # if sorted char arrays are same
        if(sorted_str1 == sorted_str2):
            print(str1 + " and " + str2 + " are anagram.")
        else:
            print(str1 + " and " + str2 + " are not anagram.")

    else:
        print(str1 + " and " + str2 + " are not anagram.") #if not same length no need check elements in str, straight away false

# to receive input from user so that can check in each example given
str1=input('Enter string 1:')
str2=input('Enter string 2:')
anagrams_checker(str1, str2)