import random

# Hàm merge cho Merge Sort
def merge(arr, left, mid, right):
    global merge_sort_comparisons
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        merge_sort_comparisons += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Hàm Merge Sort
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Hàm partition cho Quick Sort
def partition(arr, low, high):
    global quick_sort_comparisons
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        quick_sort_comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Hàm Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Đếm số so sánh
merge_sort_comparisons = 0
quick_sort_comparisons = 0

# Dữ liệu thử nghiệm
arr = [38, 27, 43, 3, 9, 82, 10]
merge_arr = arr[:]
quick_arr = arr[:]

merge_sort(merge_arr, 0, len(merge_arr) - 1)
print(f"Merge Sort số lần so sánh: {merge_sort_comparisons}")

quick_sort(quick_arr, 0, len(quick_arr) - 1)
print(f"Quick Sort số lần so sánh: {quick_sort_comparisons}")
