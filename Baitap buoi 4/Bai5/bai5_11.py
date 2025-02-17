def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():  # Nếu là số, đẩy vào ngăn xếp
            stack.append(int(char))
        elif char in "+-*/":  # Nếu là toán tử
            if len(stack) < 2:  # Kiểm tra đủ toán hạng
                return "Invalid expression"
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Thực hiện phép tính tương ứng
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                if operand2 == 0:  # Xử lý phép chia cho 0
                    return "Division by zero"
                stack.append(operand1 // operand2)  # Lấy phần nguyên
        else:
            return "Invalid character"  # Ký tự không hợp lệ

    # Kết quả cuối cùng trong ngăn xếp là giá trị của biểu thức
    if len(stack) == 1:
        return stack[-1]
    else:
        return "Invalid expression"  # Trường hợp còn dư toán hạng

# Nhập dữ liệu
T = int(input().strip())
results = []
for _ in range(T):
    expression = input().strip()
    results.append(evaluate_postfix(expression))

# Xuất kết quả
for result in results:
    print(result)
