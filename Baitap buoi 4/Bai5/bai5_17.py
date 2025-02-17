def longestValidParentheses(s):
    stack = [-1]  # Khởi tạo stack với giá trị -1 để dễ dàng tính độ dài
    max_len = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Push vị trí của dấu '(' vào stack
        else:
            stack.pop()  # Pop ra vì gặp dấu ')'
            if stack:
                max_len = max(max_len, i - stack[-1])  # Tính độ dài dãy ngoặc đúng
            else:
                stack.append(i)  # Nếu stack rỗng, đẩy vị trí của dấu ')' vào stack

    return max_len

# Nhập số lượng bộ test
T = int(input().strip())

# Xử lý từng bộ test
for _ in range(T):
    S = input().strip()
    print(longestValidParentheses(S))
