def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if (left_part[i]["score"] < right_part[j]["score"] or
                (left_part[i]["score"] == right_part[j]["score"] and left_part[i]["name"] < right_part[j]["name"])):
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Main Program
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 85},
    {"name": "David", "score": 95}
]

merge_sort(students, 0, len(students) - 1)

print("Danh sách sau khi sắp xếp:")
for student in students:
    print(student)
