def linear_search(arr, target):
    for i in range(len(arr)):         
        if arr[i] == target:          
            return i                 
    return -1                         

#arr[0]=10
#arr[1]=20
#.
#.



numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 30))   # Output: 2 (30 is at index 2)
print(linear_search(numbers, 100))  # Output: -1 (100 not found)
