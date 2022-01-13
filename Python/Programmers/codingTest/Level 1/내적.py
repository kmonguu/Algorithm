# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 반환
# a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 이다.

# 나의 코드
# 배열 a와 b의 길이만큼 반복을 통해 구한 a와 b의 내적을 answer에 담아 누적합을 구했다.

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer
  
  
# 다른 사람 풀이
# zip 함수를 통해 배열 a와 b를 튜플 쌍으로 만들어 그 곱의 합을 반환한다.

def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])



# map 함수를 이용한 방법

def solution(a, b):
    return sum(map(lambda x, y: x * y, a, b))
