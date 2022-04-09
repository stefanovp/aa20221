class MergeSort():

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

    def sort(arr, begin : int, end : int):
        if(begin >= end):
            return
        
        mid = (begin + end)//2
        MergeSort.sort(arr, begin, mid)
        MergeSort.sort(arr, mid + 1, end)
        MergeSort.merge(arr, begin, mid, end)

def main():
    print("-"*5 + " MERGE SORT QUICKTEST " + "-"*5)
    arr = [13, 64, 3423, 767, 979, 34, 123, 4, 66]
    
    print("Before sort:", end="\n")
    print(arr)

    MergeSort.sort(arr, 0, len(arr) - 1)
    
    print("After sort:", end="\n")
    print(arr)

main()