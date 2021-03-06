# n개의 숫자를 담은 배열 arr이 입력되었을 때, 이 수들의 최소공배수를 반환

# 예제
# 4개의 숫자를 담은 배열 [2, 6, 8, 14]의 결과값은 168이다.

# 내가 푼 코드
# 배열 arr의 최댓값부터 +1씩 증가시키며 arr배열 안의 요소들이 나누어 떨어지는 약수인지를 확인
# arr 배열의 모든 수를 약수로 가진다면 최소공배수가 되는 해당 값을 반환

def solution(arr):
    lcm = max(arr)
    while (True):
        cnt = 0
        for i in arr:
            if lcm % i == 0:
                cnt += 1
            else:
                lcm += 1
        if cnt == len(arr):
            break
    return lcm
         
    
# 다른 사람 풀이

def gcd(a, b): # 유클리드 호제법을 이용하여 최대공약수 구현
    while b > 0:
        a, b = b, a % b
    
    return a

def lcm(a, b): # 최소공배수
    return a * b // gcd(a, b)

def solution(arr):
    while len(arr) > 1:
        a, b = arr.pop(), arr.pop()
        arr.append(lcm(max(a, b), min(a, b)))
        
    return arr[0]
