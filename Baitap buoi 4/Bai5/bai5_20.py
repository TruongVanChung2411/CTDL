def decode_string(s):
    stack = []
    current_num = 0
    current_str = ""
    
    for char in s:
        if char.isdigit():
            # Xử lý trường hợp gặp chữ số
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Khi gặp dấu '[', lưu lại current_num và current_str vào stack
            stack.append((current_num, current_str))
            current_num, current_str = 0, ""
        elif char == ']':
            # Khi gặp dấu ']', giải mã phần trong ngoặc
            num, prev_str = stack.pop()
            current_str = prev_str + current_str * num
        else:
            # Khi gặp chữ cái, chỉ đơn giản là xây dựng current_str
            current_str += char
    
    return current_str

# Nhập số lượng bộ test
T = int(input().strip())

# Xử lý từng bộ test
for _ in range(T):
    encoded_string = input().strip()
    print(decode_string(encoded_string))
