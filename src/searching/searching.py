# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    #%BASE CASE%#
    if end >= start:
        #%Make a MidPoint%#
        middle = (start + end)//2
        #%If the Middle is the target return middle%#
        if arr[middle] == target:
            return middle
        #%Make a Smaller then Middle Case and Larger than Middle Case%#
        elif arr[middle] < target:
            return binary_search(arr, target, middle + 1, end)
        else:
            return binary_search(arr, target, start, middle - 1)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

