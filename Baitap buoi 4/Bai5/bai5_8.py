def prefix_to_postfix(expression):
    stack = []
    
    # Duyệt từ phải qua trái
    for char in reversed(expression):
        if char.isalnum():  # Nếu là toán hạng
            stack.append(char)
        else:  # Nếu là toán tử
            # Lấy hai toán hạng từ ngăn xếp
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Tạo biểu thức hậu tố
            postfix_expression = f"{operand1}{operand2}{char}"
            # Đưa kết quả vào ngăn xếp
            stack.append(postfix_expression)
    
    # Kết quả cuối cùng là biểu thức hậu tố
    return stack[-1]

# Nhập dữ liệu
T = int(input().strip())
results = []
for _ in range(T):
    expression = input().strip()
    results.append(prefix_to_postfix(expression))

# Xuất kết quả
for result in results:
    print(result)
