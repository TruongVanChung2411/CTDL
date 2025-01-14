# Hybrid Quick Sort (Quick Sort + Insertion Sort)
def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def hybrid_quick_sort(arr, low, high, threshold=10):
    if high - low + 1 <= threshold:
        insertion_sort(arr, low, high)
    else:
        if low < high:
            pi = partition(arr, low, high)
            hybrid_quick_sort(arr, low, pi - 1, threshold)
            hybrid_quick_sort(arr, pi + 1, high, threshold)
