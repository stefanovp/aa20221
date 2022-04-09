import time
import os

# Insertion Sort

#função pra trocar um valor com no array com outro na posição anterior
def swap (arr, pos):
    temp = arr[pos]
    arr[pos] = arr[pos-1]
    arr[pos-1] = temp
    

def insertion_sort(array):
    courrent_pos = 1
    
    while courrent_pos < len(array):
        temp_pos = courrent_pos
        
        while temp_pos > 0 and array[temp_pos-1] > array[temp_pos]:
            swap(array, temp_pos)
            temp_pos -= 1
            
        courrent_pos += 1
    return
      

      
def main():
    
    #vc tem q botar o seu arquivo DataSort.in em C:\Users\[seu user]
    home = os.path.expanduser("~")
    f = open(home + "\\DataSort.in", "r")
    
    main_array = []
    
    i = 0
    for line in f:
        line = line.strip()
        
        #limitar número de linhas lidas do arq
        i += 1
        if i > 2000: break 
        
        #tirar linhas zuadas do arquivo
        if not line.isdecimal(): 
            continue
        
        line = int(line)
        main_array.append(line)
        
    f.close()
    
    before = time.time() #hora de inicio
    
    insertion_sort(main_array)
    
    after = time.time() #hora do fim
    total = (after - before) * 1000 #pega o tempo em ms
    
    print(main_array)
    print('Total runtime: %0.2f ms' % total)
    
    return 0


main()