def evaluate_prefix(expression):
    stack = []
    
    # Duyệt từ phải sang trái
    for char in reversed(expression):
        if char.isdigit():  # Nếu là số, đẩy vào ngăn xếp
            stack.append(int(char))
        elif char in "+-*/":  # Nếu là toán tử
            if len(stack) < 2:  # Kiểm tra đủ toán hạng
                return "Invalid expression"
            operand1 = stack.pop()
            operand2 = stack.pop()

            # Thực hiện phép tính
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                if operand2 == 0:  # Kiểm tra chia cho 0
                    return "Division by zero"
                stack.append(operand1 // operand2)  # Lấy phần nguyên
        else:
            return "Invalid character"  # Ký tự không hợp lệ

    # Kết quả cuối cùng
    return stack[-1] if len(stack) == 1 else "Invalid expression"

# Nhập dữ liệu
T = int(input().strip())
results = []
for _ in range(T):
    expression = input().strip()
    results.append(evaluate_prefix(expression))

# Xuất kết quả
for result in results:
    print(result)
