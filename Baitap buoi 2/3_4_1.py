import random

from bt02.vd5 import partition


def randomized_partition(arr, low, high):

    pivot_index = random.randint(low, high)

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    return partition(arr, low, high)


def quick_sort_randomized(arr, low, high):

    if low < high:

        p = randomized_partition(arr, low, high)

        quick_sort_randomized(arr, low, p-1)

        quick_sort_randomized(arr, p+1, high)