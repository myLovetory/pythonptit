def submatrix_sum(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    # Tính toán các tổng phụ của ma trận
    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]

            # Kiểm tra tổng phụ có bằng k không
            sub_sum = 0
            for i in range(rows):
                sub_sum += temp[i]
                if sub_sum == k:
                    count += 1
                if sub_sum - k in temp:
                    count += temp.count(sub_sum - k)

    return count


m = int(input())
n = int(input())
k = int(input())


matrix = []

for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)


result = submatrix_sum(matrix, k)
print( k, result)