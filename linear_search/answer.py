def first_occurrence(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example
print(first_occurrence([5, 8, 3, 8, 9], 8))   # Output: 1



def last_occurrence(arr, target):
    for i in range(len(arr)-1, -1, -1):   # loop backwards
        if arr[i] == target:
            return i
    return -1

# Example
print(last_occurrence([5, 8, 3, 8, 9], 8))   # Output: 3



def all_occurrences(arr, target):
    indexes = []
    for i in range(len(arr)):
        if arr[i] == target:
            indexes.append(i)
    return indexes if indexes else -1

# Example
print(all_occurrences([2, 5, 7, 5, 9, 5], 5))   # Output: [1, 3, 5]



def first_even(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:   # condition check
            return i
    return -1

# Example
print(first_even([11, 15, 7, 20, 9]))   # Output: 3
