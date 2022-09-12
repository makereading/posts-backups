def binary_search(arr, key, start, end):
    if start == end:
        if arr[start] > key:
            return start
        else:
            return start+1
 
    if start > end:
        return start
 
    mid = (start+end)//2
    if arr[mid] < key:
        return binary_search(arr, key, mid+1, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid-1)
    else:
        return mid
 
def insertion_sort(arr):
    total_num = len(arr)
    for i in range(1, total_num):
        key = arr[i]
        j = binary_search(arr, key, 0, i-1)
        arr = arr[:j] + [key] + arr[j:i] + arr[i+1:]
    return arr
 

sorted_array = insertion_sort([29, 10, 14, 37, 14])
print("Sorted Array : ", sorted_array)