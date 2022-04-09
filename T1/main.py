import time

from merge_sort import MergeSort
from file_utils import AAFileUtils

def instrumented_merge_sort(dataset_data):
        start = time.time()
        MergeSort.sort(dataset_data, 0, len(dataset_data) - 1)
        stop = time.time()
        return stop - start

def main():
    
    # Load data
    test_datasets = AAFileUtils.load_test_subjects("T1/test_data/DataSortB.txt")
    print('Test data successfully loaded')
    print('Test Datasets:')
    for set_name in test_datasets:
        print(f"dataset {set_name} ({len(test_datasets[set_name])} lines)")
    
    # Run sorts
    for dataset_name in test_datasets:
        dataset_data = test_datasets[dataset_name]
        
        elapsed = instrumented_merge_sort(dataset_data)
        print(f"Sorted {dataset_name}. ElapsedTime = {elapsed}s")

main()