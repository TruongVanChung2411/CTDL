def postfix_to_prefix(expression):
    stack = []
    
    # Duyệt từ trái qua phải
    for char in expression:
        if char.isalnum():  # Nếu là toán hạng
            stack.append(char)
        else:  # Nếu là toán tử
            # Lấy hai toán hạng từ ngăn xếp
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Tạo biểu thức tiền tố
            prefix_expression = f"{char}{operand1}{operand2}"
            # Đưa kết quả vào ngăn xếp
            stack.append(prefix_expression)
    
    # Kết quả cuối cùng là biểu thức tiền tố
    return stack[-1]

# Nhập dữ liệu
T = int(input().strip())
results = []
for _ in range(T):
    expression = input().strip()
    results.append(postfix_to_prefix(expression))

# Xuất kết quả
for result in results:
    print(result)
2