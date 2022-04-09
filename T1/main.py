import time

from insertion_sort import InsertionSort
from merge_sort import MergeSort
from file_utils import AAFileUtils

def instrumented_merge_sort(dataset_data):
        start = time.time()
        MergeSort.sort(dataset_data, 0, len(dataset_data) - 1)
        stop = time.time()
        return stop - start

def instrumented_insertion_sort(dataset_data):
        start = time.time()
        InsertionSort.sort(dataset_data)
        stop = time.time()
        return stop - start

def main():
    
    # Load data into memory
    test_datasets = AAFileUtils.load_test_subjects("T1/test_data/DataSortB.txt")
    print('Test data successfully loaded')
    print('Test Datasets:')
    for set_name in test_datasets:
        print(f"dataset {set_name} ({len(test_datasets[set_name])} lines)")
    print()
    
    # Run sorts
    # ATENÇÂO: estamos sortando os datasets inplace, então somente um tipo
    # de sort abaixo pode estar descomentado. Caso contrario, tentaremos
    # sortaer dados já sorteados. 
    # ps ctrl + k + c para comment varias linhas, ctrl + k + u para uncomment
    for dataset_name in test_datasets:
        dataset_data = test_datasets[dataset_name]
        
        elapsed = instrumented_insertion_sort(dataset_data)
        print(f"Sorted {dataset_name}. ElapsedTime = {elapsed}s")

        # elapsed = instrumented_merge_sort(dataset_data)
        # print(f"Sorted {dataset_name}. ElapsedTime = {elapsed}s")

main()