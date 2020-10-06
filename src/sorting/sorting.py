# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    arrA_pointer = arrB_pointer = 0
    arrA_length, arrB_length = len(arrA), len(arrB)

    for _ in range(elements):
        if arrA_pointer < arrA_length and arrB_pointer < arrB_length:
            if arrA[arrA_pointer] <= arrB[arrB_pointer]:
                merged_arr[arrA_pointer + arrB_pointer] = arrA[arrA_pointer]
                arrA_pointer += 1
            else:
                merged_arr[arrA_pointer + arrB_pointer] = arrB[arrB_pointer]
                arrB_pointer += 1

        elif arrA_pointer == arrA_length:
            merged_arr[arrA_pointer + arrB_pointer] = arrB[arrB_pointer]
            arrB_pointer += 1

        elif arrB_pointer == arrB_length:
            merged_arr[arrA_pointer + arrB_pointer] = arrA[arrA_pointer]
            arrA_pointer += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1: return arr
    midpoint = int(len(arr) // 2)
    arrA = merge_sort(arr[:midpoint])
    arrB = merge_sort(arr[midpoint:])

    return merge(arrA, arrB)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

