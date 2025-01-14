import time
import random

# Hàm merge cho Merge Sort
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Tạo các mảng con
    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]

    # Chỉ số khởi đầu của các mảng
    i = j = 0
    k = left

    # Hợp nhất hai mảng con
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Sao chép các phần tử còn lại của L
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Sao chép các phần tử còn lại của R
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

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Đo thời gian thực hiện
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

# Tạo mảng ngẫu nhiên và đo thời gian
sizes = [5000, 10000, 20000]
for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]
    print(f"\nKích thước mảng: {size}")

    arr_copy = arr[:]
    bubble_time = measure_time(lambda x: bubble_sort(x), arr_copy)
    print(f"Bubble Sort: {bubble_time:.2f} giây")

    arr_copy = arr[:]
    merge_time = measure_time(lambda x: merge_sort(x, 0, len(x) - 1), arr_copy)
    print(f"Merge Sort: {merge_time:.2f} giây")
