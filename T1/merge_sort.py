import math

def merge(arr, begin : int, mid : int, end : int):
    i = begin
    j = mid + 1
    k = begin
    result = arr[:]
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            result[k] = arr[i]
            i += 1
            k += 1
        else:
            result[k] = arr[j]
            j += 1
            k += 1
    
    while i <= mid:
        result[k] = arr[i]
        i += 1
        k += 1
    while j <= end:
        result[k] = arr[j]
        j += 1
        k += 1  

    arr[:] = result

def merge_sort(arr, begin : int, end : int):
    if(begin >= end):
        return
    
    mid = (begin + end)//2
    merge_sort(arr, begin, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, begin, mid, end)

def main():
    arr = [12, 11, 13, 5, 6, 7]
    print("Before sort:", end="\n")
    print(arr)
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)

main()