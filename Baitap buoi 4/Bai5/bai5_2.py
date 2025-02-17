def min_changes_to_make_valid(S):
    balance = 0  # Đếm số ngoặc mở dư thừa cần đóng
    changes = 0  # Số lần đổi chiều để xử lý dấu ngoặc đóng dư thừa

    for char in S:
        if char == '(':
            balance += 1
        else:  # char == ')'
            if balance > 0:
                balance -= 1  # Đã đóng một cặp ngoặc đúng
            else:
                changes += 1  # Dấu ')' dư thừa, cần đổi thành '('

    # Tổng số thay đổi là số dấu ')' dư thừa và số dấu '(' dư thừa
    return changes + balance

# Nhập dữ liệu
T = int(input().strip())
results = []
for _ in range(T):
    S = input().strip()
    results.append(min_changes_to_make_valid(S))

# Xuất kết quả
for result in results:
    print(result)
