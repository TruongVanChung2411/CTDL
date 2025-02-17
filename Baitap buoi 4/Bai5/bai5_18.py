def find_next_greater_freq(n, arr):
    # Bước 1: Tính số lần xuất hiện của mỗi phần tử trong mảng
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Bước 2: Duyệt mảng từ phải sang trái
    ans = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        # Kiểm tra stack xem có phần tử nào có số lần xuất hiện lớn hơn
        while stack and freq[stack[-1]] <= freq[arr[i]]:
            stack.pop()

        # Nếu stack không rỗng, phần tử ở đỉnh stack là kết quả
        if stack:
            ans[i] = stack[-1]
        
        # Đẩy phần tử hiện tại vào stack
        stack.append(arr[i])

    return ans

# Nhập số lượng bộ test
T = int(input().strip())

# Xử lý từng bộ test
for _ in range(T):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    
    # Tính toán kết quả cho mỗi bộ test
    result = find_next_greater_freq(n, arr)
    print(" ".join(map(str, result)))
