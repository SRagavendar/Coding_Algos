"""
The nth root of a number
For example the 3rd root or cube root of 27 is 3 as 3 * 3 * 3 = 27.
So looking for the nth root we can check if we have found it by taking the current estimate and raising it to the power of n.
Haven't handled with the recursion depth limit yet.
"""

def binary_search_nth_root(number, nth_root, min_val, max_val, accuracy):
    hi = max_val
    lo = min_val
    while lo < hi:
        mid_val = (hi + lo) / 2
        approx = round(mid_val ** nth_root, accuracy)
        print("approx: %s, mid_val: %s, hi: %s, lo: %s" % (approx, mid_val, hi, lo))
        if approx == number:
            return mid_val
        elif approx > number:
            hi = mid_val
        else:
            lo = mid_val
    return -1

def binary_search_find_root(number, min_v, max_v, accuracy, n):
    if max_v <= min_v:
        return -1
    mid_val = (max_v + min_v) / 2
    if round(mid_val ** n, accuracy) == number:
        return mid_val
    elif mid_val ** n > number:
        return binary_search_find_root(number, min_v, mid_val, accuracy, n)
    elif mid_val ** n < number:
        return binary_search_find_root(number, mid_val, max_v, accuracy, n)

number = 1996
accuracy = 90
nth_dimension_root = 2

min_v = 0
max_v = 100000000
nth_root_1 = binary_search_find_root(number, min_v, max_v, accuracy, nth_dimension_root)
nth_root_2 = binary_search_nth_root(number, nth_dimension_root, min_v, max_v, accuracy)
print(nth_root_1)
print(nth_root_2)