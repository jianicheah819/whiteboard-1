list1 = [21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28] #initialize the list to sort
#define function to sort the list as no library function allow to use
def ascending_sort(list1):
    n=len(list1) #to know the length of list

    for i in range(n): #loop each element in list
        for j in range (0, n-i-1): #compare btw elements and switch if wrong order
            if list1[j] > list1[j+1]: #if current element is greater than next element 
                list1[j], list1[j+1] = list1[j+1], list1[j] #then swap the element

ascending_sort(list1) #call function
print(list1) #print

# Bonus ans:
# Space Complexity Analysis:
# O(1) where the space is constant for the loop to run
# Time Complexity Analysis:
# The time complexity will be O(n^2) as inside a for loop have another loop to run. The inner loop require the current loop number of outer loop to run
# so the time will be power of 2. 