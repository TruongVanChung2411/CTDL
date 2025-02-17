def stock_span(n, prices):
    # Mảng kết quả để lưu nhịp chứng khoán
    span = [0] * n
    # Stack sẽ lưu các chỉ số của giá chứng khoán
    stack = []
    
    for i in range(n):
        # Tính nhịp chứng khoán cho ngày thứ i
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()  # Pop các phần tử không thỏa mãn điều kiện
        
        # Nếu stack rỗng, có nghĩa là không có giá trị nào nhỏ hơn hoặc bằng với giá hiện tại
        # Nhịp chứng khoán của ngày thứ i chính là số ngày liên tiếp tính từ i
        span[i] = i + 1 if not stack else i - stack[-1]
        
        # Thêm chỉ số ngày i vào stack
        stack.append(i)
    
    return span

# Nhập số lượng bộ test
T = int(input().strip())

# Xử lý từng bộ test
for _ in range(T):
    n = int(input().strip())  # Số ngày
    prices = list(map(int, input().strip().split()))  # Giá chứng khoán mỗi ngày
    
    # Tính nhịp chứng khoán cho mỗi bộ test
    result = stock_span(n, prices)
    print(" ".join(map(str, result)))
