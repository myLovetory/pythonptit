def count_pytago_triplets(N):
    count = 0

    for a in range(1, N):
        for b in range(a, N):
            c_squared = (a*a + b*b) % N
            c = int(c_squared**0.5)
            
            if c >= a and c <= N-1 and c*c == c_squared:
                count += 1
    
    return count

# Đọc giá trị N
N = int(input())

# Tính và in ra kết quả
result = count_pytago_triplets(N)
print(result)