class ShellSort():
    def sort_potencia_de_2(array):
        print("sort algothm here")

    def sort_fibonacci(array):
        print("sort algothm here")


# Para testar sem precisar do arquivo
def main():
    print("-"*5 + " SHELL SORT QUICKTEST " + "-"*5)
    main_array1 = [13, 64, 3423, 767, 979, 34, 123, 4, 66]
    main_array2 = [13, 3423, 767, 64, 4, 979, 123, 34, 66]
    
    print("Before sort:", end="\n")
    print(main_array1)
    print(main_array2)

    ShellSort.sort_potencia_de_2(main_array1)
    ShellSort.sort_fibonacci(main_array2)

    print("After sort:", end="\n")
    print(main_array1)
    print(main_array2)

main()
