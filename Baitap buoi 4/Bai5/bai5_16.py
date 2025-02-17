def largestRectangleArea(heights):
    n = len(heights)
    stack = []
    max_area = 0
    i = 0

    # Duyệt qua tất cả các cột trong biểu đồ
    while i < n:
        if not stack or heights[stack[-1]] <= heights[i]:
            stack.append(i)
            i += 1
        else:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)

    # Xử lý các phần tử còn lại trong stack
    while stack:
        h = heights[stack.pop()]
        width = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, h * width)

    return max_area

# Nhập số lượng bộ test
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    heights = list(map(int, input().strip().split()))
    print(largestRectangleArea(heights))
