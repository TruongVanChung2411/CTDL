def max_valid_parentheses_length(s):
    stack = [-1]  # Đặt một phần tử -1 vào đầu stack để dễ dàng tính toán độ dài.
    max_len = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Lưu chỉ số của dấu ngoặc mở
        else:
            stack.pop()  # Xóa dấu ngoặc mở đã khớp
            if stack:
                max_len = max(max_len, i - stack[-1])  # Tính độ dài đoạn đúng
            else:
                stack.append(i)  
                
    return max_len

# Đọc số lượng bộ test
T = int(input().strip())

# Xử lý từng bộ test
for _ in range(T):
    s = input().strip()
    print(max_valid_parentheses_length(s))
