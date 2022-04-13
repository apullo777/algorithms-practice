from array import array


def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


test = [1, 4, 6, 9, 3, 5, 6, 7, 1, 3, 82748, 13761, 1873, 8173,991, 8, 3]
print(quickSort(test))
