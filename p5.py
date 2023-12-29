def symmetric_difference(list1, list2):
    # Convert the lists to sets to reduce time checking the elements
    set1 = set(list1)
    set2 = set(list2)

    # Find elements that are unique in each set 
    seta = set1.difference(set2)
    setb = set2.difference(set1)

    # Combine the elements from both set and change to list
    symmetric_difference = list(seta.union(setb)) 

    return symmetric_difference

list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]
result = symmetric_difference(list1, list2)
print(result)

# Bonus ans:
# Space Complexity Analysis:
# The space complexity of this solution is O(min(N, M)), where N and M are the lengths of the two input lists. 
#This is because we use sets (set1 and set2) to store elements, and their sizes are determined by the minimum length of the two input lists.
# Time Complexity Analysis:
# Converting lists to sets takes O(N + M) time, where N and M are the lengths of the input lists.
# Two operation where to find the unique element in the set and union both set take the O(N+M) time. 
# Overall, the time complexity is O(N + M), where N and M are the lengths of the input lists.