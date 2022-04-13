# Return index of an item in an array if present, else -1 
def binarySearch(arr, low, high, item):
    # check base case
    if high >= low:
        mid = (high + low) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            return binarySearch(arr, low, mid - 1, item)
        else:
            return binarySearch(arr, mid + 1, high, item)
        
    else:
        return -1
    

test =  [1, 4, 6, 9, 3, 5, 6, 7, 1, 3, 82748, 13761, 1873, 8173,991, 8, 3]
x = 4
result = binarySearch(test, 0 , len(test) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
