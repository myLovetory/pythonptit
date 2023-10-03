def prime_factorization_and_sum(N):
    prime_sum = 0
    for _ in range(N):
        num = int(input())
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                prime_sum += i
        if num > 1:
            prime_sum += num
    return prime_sum

# Đọc số lượng số nguyên từ input
N = int(input())

# Gọi hàm prime_factorization_and_sum và in ra kết quả
result = prime_factorization_and_sum(N)
print("Tổng các ước số nguyên tố:", result)