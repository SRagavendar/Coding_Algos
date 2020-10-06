  
"""
Precondition: arr is in sorted order
Iterative binary searching
How it works: look at middle item in arr, if target < mid split that half and binary search it, else look at the other half. This reduces the search size be half each time leading to the log n complexity
"""

def binary_search_iterative(array, target):
    lo = 0
    high = len(array) - 1
    while True:
        if lo > high:
            return -1
        mid_index = (lo + high)//2
        if target == array[mid_index]:
            return mid_index
        elif target > array[mid_index]:
            lo = mid_index + 1
        else:
            high = mid_index - 1
    return -1

'''
def binary_search(array, target):
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
'''
#    0   1   2   3   4   5   6   7   8   9   10
a = [10, 20, 30, 55, 50, 45, 69, 78, 83, 95, 110]
target = 69

print(binary_search_iterative(a, target))

#print(binary_search(a, target))