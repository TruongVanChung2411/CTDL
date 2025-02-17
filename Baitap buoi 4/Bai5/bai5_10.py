def postfix_to_infix(expression):
    stack = []

    # Duyệt từng ký tự trong biểu thức hậu tố
    for char in expression:
        if char.isalnum():  # Nếu là toán hạng
            stack.append(char)
        else:  # Nếu là toán tử
            # Lấy hai toán hạng từ ngăn xếp
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Tạo biểu thức trung tố với dấu ngoặc
            infix_expression = f"({operand1}{char}{operand2})"
            # Đưa kết quả vào ngăn xếp
            stack.append(infix_expression)

    # Kết quả cuối cùng trong ngăn xếp là biểu thức trung tố
    return stack[-1]

# Nhập dữ liệu
T = int(input().strip())
results = []
for _ in range(T):
    expression = input().strip()
    results.append(postfix_to_infix(expression))

# Xuất kết quả
for result in results:
    print(result)
