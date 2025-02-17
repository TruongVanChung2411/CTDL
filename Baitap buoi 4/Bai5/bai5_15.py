def find_next_greater_smaller(arr):
    n = len(arr)
    nge = [-1] * n  # Lưu phần tử lớn hơn tiếp theo
    stack = []

    # Tìm Next Greater Element (NGE) cho mỗi phần tử
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            nge[idx] = arr[i]
        stack.append(i)

    # Tìm Next Smaller Element (NSE) cho NGE
    result = []
    for i in range(n):
        if nge[i] == -1:
            result.append(-1)
        else:
            # Tìm phần tử nhỏ hơn đầu tiên sau NGE
            j = i + 1
            found = -1
            while j < n:
                if arr[j] < nge[i]:
                    found = arr[j]
                    break
                j += 1
            result.append(found)

    return result

# Nhập dữ liệu
T = int(input().strip())
results = []
for _ in range(T):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    results.append(find_next_greater_smaller(arr))

# Xuất kết quả
for res in results:
    print(" ".join(map(str, res)))
