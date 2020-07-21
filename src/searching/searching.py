# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    
    # exit out of recursion and indicate finding the end
    if not start <= end:
        return -1
    # var create value of middle of list 
    mid = (start + end)//2
    # mid is less then move right 
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    # mid is greater than move left
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    # target = the mid initial input number
    else:
        return mid

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively

    def agnostic_binary_search(arr, target):
        # Your code here
        pass
