def are_expressions_equal(P1, P2):
    # So sánh độ dài trước để tối ưu
    if len(P1) != len(P2):
        return "NO"

    # So sánh từng ký tự trong P1 và P2
    for c1, c2 in zip(P1, P2):
        if c1 != c2:
            return "NO"

    return "YES"

# Đọc dữ liệu đầu vào
T = int(input().strip())
results = []
for _ in range(T):
    P1 = input().strip()
    P2 = input().strip()
    results.append(are_expressions_equal(P1, P2))

# Xuất kết quả
for result in results:
    print(result)
