def intersect_list(list1, list2):
    # Convert the lists to sets to reduce time complexity 
    set1 = set(list1)
    set2 = set(list2)

    # Initialize an empty list to store the intersection
    intersection = []

    # Iterate through the elements of set1 and check if they are in set2
    for n in set1:
        if n in set2:
            intersection.append(n) #if element in set 1 also in set2 then will insert the element into intersection list

    return intersection

list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]
result = intersect_list(list1, list2)
print(result)

# Bonus ans:
# Space Complexity Analysis:
# The space complexity of this solution is O(min(N, M)), where N and M are the lengths of the two input lists. 
#This is because we use sets (set1 and set2) to store elements, and their sizes are determined by the minimum length of the two input lists.
# Time Complexity Analysis:
# Converting lists to sets takes O(N + M) time, where N and M are the lengths of the input lists.
# The loop that iterates through the elements of set1 takes O(min(N, M)) time because it iterates through the smaller set.
# Overall, the time complexity is O(N + M), where N and M are the lengths of the input lists.