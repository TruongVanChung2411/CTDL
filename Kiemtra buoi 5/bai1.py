from collections import deque

def max_kernel(num_list, k):
    result = []
    dq = deque()
    
    for i in range(len(num_list)):
        # Xóa các phần tử không còn trong cửa sổ
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Xóa các phần tử nhỏ hơn phần tử hiện tại trong hàng đợi
        while dq and num_list[dq[-1]] < num_list[i]:
            dq.pop()

        dq.append(i)

        # Bắt đầu lấy giá trị lớn nhất khi cửa sổ đủ k phần tử
        if i >= k - 1:
            result.append(num_list[dq[0]])
    
    return result

# Test case
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))  # Output: [5, 5, 5, 5, 10, 12, 33, 33]
