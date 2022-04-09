class InsertionSort():
    
    # Função pra trocar um valor com no array com outro na posição anterior
    def swap (arr, pos):
        temp = arr[pos]
        arr[pos] = arr[pos-1]
        arr[pos-1] = temp

    def sort(array):
        courrent_pos = 1
        
        while courrent_pos < len(array):
            temp_pos = courrent_pos
            
            while temp_pos > 0 and array[temp_pos-1] > array[temp_pos]:
                InsertionSort.swap(array, temp_pos)
                temp_pos -= 1
                
            courrent_pos += 1
        return

def main():    
    print("-"*5 + " INSERTION SORT QUICKTEST " + "-"*5)
    main_array = [13, 64, 3423, 767, 979, 34, 123, 4, 66]
    
    print("Before sort:", end="\n")
    print(main_array)

    InsertionSort.sort(main_array)
    
    print("After sort:", end="\n")
    print(main_array)

main()