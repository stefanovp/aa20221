class QuickSort():
    def sort(array):
        print("sort algothm here")

# Para testar sem precisar do arquivo
def main():
    print("-"*5 + " QUICK SORT QUICKTEST " + "-"*5)
    main_array = [13, 64, 3423, 767, 979, 34, 123, 4, 66]
    
    print("Before sort:", end="\n")
    print(main_array)

    QuickSort.sort(main_array)
    
    print("After sort:", end="\n")
    print(main_array)

main()
