# 자연수 n이 매개변수로 주어질 때, n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 수 x를 반환

# 내가 푼 풀이
# n의 범위가 3 ≤ n ≤ 1,000,000 이므로 n을 나누었을 때 나머지가 1이 나오게 하는 x의 최솟값은 2이다.
# n을 x로 나눈 나머지가 1이라면 x를 반환, 아니라면 x 값을 1 증가

def solution(n):
    x = 2
    while x < n:
        if n % x == 1:
            return x
        else:
            x += 1

            
            
            
# 다른 사람 풀이
# 나머지가 1이 되는 수는 (n-1)의 제곱근보다 클 수 없음을 이용

def solution(n):
    for x in range(2, int((n - 1) ** 0.5) + 1):
        if (n - 1) % x == 0:
            return x
    
    return n - 1
