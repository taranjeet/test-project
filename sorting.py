from typing import List

def naive_bubble_sort(arr: List[int]) -> None:
    """
    Sorts the given list of integers in ascending order using the naive bubble sort algorithm.

    :param arr: List of integers to be sorted
    """
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main() -> None:
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array is:", arr)

    naive_bubble_sort(arr)
    print("Sorted array is:", arr)

if __name__ == "__main__":
    main()