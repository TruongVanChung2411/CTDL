from datetime import datetime

def partition(arr, low, high):
    pivot = datetime.strptime(arr[high]["last_login"], "%Y-%m-%d")
    i = low - 1

    for j in range(low, high):
        if datetime.strptime(arr[j]["last_login"], "%Y-%m-%d") >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Main Program
records = [
    {"user": "Alice", "last_login": "2025-01-10"},
    {"user": "Bob", "last_login": "2025-01-12"},
    {"user": "Charlie", "last_login": "2025-01-11"}
]

quick_sort(records, 0, len(records) - 1)

print("Danh sách sau khi sắp xếp:")
for record in records:
    print(record)
