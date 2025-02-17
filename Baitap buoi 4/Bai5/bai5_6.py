# Hàm xác định độ ưu tiên của các toán tử
def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0

# Hàm chuyển biểu thức trung tố sang hậu tố
def infix_to_postfix(expression):
    result = []  # Kết quả hậu tố
    stack = []   # Ngăn xếp lưu các toán tử và dấu ngoặc

    for char in expression:
        if char.isalnum():  # Nếu là toán hạng (chữ hoặc số)
            result.append(char)
        elif char == '(':   # Nếu là dấu mở ngoặc
            stack.append(char)
        elif char == ')':   # Nếu là dấu đóng ngoặc
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Bỏ dấu mở ngoặc '(' khỏi ngăn xếp
        else:  # Nếu là toán tử
            while (stack and precedence(stack[-1]) >= precedence(char)):
                result.append(stack.pop())
            stack.append(char)

    # Đưa tất cả toán tử còn lại trong ngăn xếp vào kết quả
    while stack:
        result.append(stack.pop())

    return ''.join(result)

# Nhập dữ liệu
T = int(input().strip())
results = []
for _ in range(T):
    expression = input().strip()
    results.append(infix_to_postfix(expression))

# Xuất kết quả
for result in results:
    print(result)
