from itertools import combinations

def remove_parentheses(expression, pairs_to_remove):
    """Hàm xóa các cặp dấu ngoặc dựa trên danh sách chỉ số cặp dấu ngoặc cần xóa"""
    to_remove = set()  # Tập các vị trí cần xóa
    for open_index, close_index in pairs_to_remove:
        to_remove.add(open_index)
        to_remove.add(close_index)

    result = []  # Biểu thức sau khi xóa dấu ngoặc
    for i, char in enumerate(expression):
        if i not in to_remove:
            result.append(char)

    return ''.join(result)

def find_all_valid_expressions(expression):
    """Tìm tất cả các biểu thức hợp lệ bằng cách xóa dấu ngoặc"""
    stack = []
    pairs = []  # Danh sách các cặp ngoặc (chỉ số của dấu '(' và ')')

    # Xác định vị trí các cặp ngoặc
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            open_index = stack.pop()
            pairs.append((open_index, i))

    # Tập hợp kết quả lưu các biểu thức hợp lệ
    results = set()

    # Sinh tất cả các tổ hợp dấu ngoặc cần xóa (bỏ ít nhất 1 cặp)
    n = len(pairs)
    for r in range(1, n + 1):
        for combination in combinations(pairs, r):
            new_expression = remove_parentheses(expression, combination)
            results.add(new_expression)

    # Chuyển kết quả thành danh sách và sắp xếp theo thứ tự từ điển
    sorted_results = sorted(results)
    return sorted_results

# Đọc dữ liệu đầu vào
expression = input().strip()

# Tìm tất cả các biểu thức hợp lệ và in kết quả
valid_expressions = find_all_valid_expressions(expression)
for expr in valid_expressions:
    print(expr)
