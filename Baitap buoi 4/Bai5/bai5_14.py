def smallest_number_from_pattern(S):
    result = []
    stack = []
    num = 1  # Bắt đầu từ số 1

    for char in S:
        stack.append(num)
        num += 1
        if char == 'I':  # Nếu gặp ký tự 'I', pop toàn bộ stack vào kết quả
            while stack:
                result.append(stack.pop())

    # Thêm số cuối cùng vào stack và pop toàn bộ
    stack.append(num)
    while stack:
        result.append(stack.pop())

    # Chuyển kết quả thành chuỗi
    return ''.join(map(str, result))

# Nhập dữ liệu
T = int(input().strip())
results = []
for _ in range(T):
    S = input().strip()
    results.append(smallest_number_from_pattern(S))

# Xuất kết quả
for result in results:
    print(result)
