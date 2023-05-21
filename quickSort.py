"""
Quick sort algorithm using recurtion in python
Time Complexity: O( N logN ) -- O( N2 )
"""


def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quickSort(arr: list, low: int, high: int):
    if low < high:
        pivotPosition = partition(arr, low, high)
        quickSort(arr, low, pivotPosition - 1)
        quickSort(arr, pivotPosition + 1, high)


colors = [1, 7, 4, 1, 10, 9, -2]
size = len(colors)
quickSort(colors, 0, size-1)
print(colors)
