def has_redundant_parentheses(expression):
    stack = []
    for char in expression:
        if char == ')':
            top = stack.pop()
            elements_inside = 0

            while top != '(':
                elements_inside += 1
                top = stack.pop()

            # Nếu không có ký tự nào nằm giữa cặp ngoặc
            if elements_inside == 0:
                return True
        else:
            stack.append(char)

    return False


# Nhập và xử lý dữ liệu
T = int(input("Nhập số bộ test: "))
results = []
for _ in range(T):
    expression = input("Nhập biểu thức: ")
    if has_redundant_parentheses(expression):
        results.append("Yes")
    else:
        results.append("No")

# Xuất kết quả
for result in results:
    print(result)
