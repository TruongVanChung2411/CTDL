def precedence(op):
    """Trả về độ ưu tiên của toán tử."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(expression):
    """Chuyển biểu thức trung tố sang hậu tố."""
    stack = []
    postfix = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isdigit():  # Xử lý số nguyên (có thể nhiều chữ số)
            num = char
            while i + 1 < len(expression) and expression[i + 1].isdigit():
                num += expression[i + 1]
                i += 1
            postfix.append(num)
        elif char == '(':  # Dấu mở ngoặc
            stack.append(char)
        elif char == ')':  # Dấu đóng ngoặc
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Loại bỏ dấu '(' khỏi ngăn xếp
        else:  # Toán tử
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)
        i += 1

    # Đưa các toán tử còn lại vào hậu tố
    while stack:
        postfix.append(stack.pop())

    return postfix

def evaluate_postfix(postfix):
    """Tính giá trị biểu thức hậu tố."""
    stack = []
    for char in postfix:
        if char.isdigit():  # Nếu là số, đẩy vào ngăn xếp
            stack.append(int(char))
        else:  # Nếu là toán tử
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 // operand2)  # Lấy phần nguyên
    return stack[-1]

# Nhập dữ liệu
T = int(input().strip())
results = []
for _ in range(T):
    expression = input().strip()
    postfix = infix_to_postfix(expression)
    result = evaluate_postfix(postfix)
    results.append(result)

# Xuất kết quả
for result in results:
    print(result)
