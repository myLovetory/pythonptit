def check_dodac(A):
    N = len(A)
    unique_elements = set()
    
    for i in range(N-1):
        for j in range(i+2, N+1):
            sub_array = A[i:j]
            unique_elements.clear()
            
            for element in sub_array:
                if element in unique_elements:
                    return "NO"
                unique_elements.add(element)
    
    return "YES"

# Đọc số lượng bộ test
T = int(input())

for _ in range(T):
    # Đọc số lượng phần tử và dãy số
    N = int(input())
    A = list(map(int, input().split()))
    
    # Kiểm tra và in kết quả
    result = check_dodac(A)
    print(result)