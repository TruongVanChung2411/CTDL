def remove_parentheses(expression):
    stack = []  # Dùng để lưu trạng thái của dấu trước mỗi dấu '('
    result = []  # Kết quả biểu thức sau khi bỏ ngoặc
    sign = 1  # Dấu hiện tại (1: dương, -1: âm)

    for i, char in enumerate(expression):
        if char == '+':
            if sign == 1:
                result.append('+')
            else:
                result.append('-')
        elif char == '-':
            if sign == 1:
                result.append('-')
            else:
                result.append('+')
        elif char == '(':
            # Nếu có dấu '-' trước dấu ngoặc, đổi trạng thái
            if i > 0 and expression[i - 1] == '-':
                sign = -sign
            stack.append(sign)
        elif char == ')':
            # Trở về trạng thái trước dấu ngoặc
            sign = stack.pop()
        else:
            # Là ký tự toán hạng (a, b, c, ...)
            result.append(char)

    return ''.join(result)


# Nhập dữ liệu
T = int(input().strip())
results = []
for _ in range(T):
    expression = input().strip()
    results.append(remove_parentheses(expression))

# Xuất kết quả
for result in results:
    print(result)
