# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 반환

# 효율성 테스트에서 실패한 코드 (75점)
# 더해지는 값 j의 범위가 n까지로 모든 수를 더하여 확인하는데, 모든 경우를 더하여 방법의 수를 구하기 때문에 효율성에서 문제가 생기는 것으로 판단
# j의 범위를 수정한다면 효율성 테스트에서 실패하지 않을 것 같음

def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if(sum == n):
                answer += 1

    return answer


# 내가 푼 코드
# 틀린 부분 : 마지막 조건문에서 sum이 n보다 커질 경우를 고려하지 못하여 sum == n일 때 answer에 +1을 하고 멈추는 것이 아닌
#             j의 주어진 범위까지 다 돌기 때문에 효율성에서 문제가 생겼음

def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if(sum == n):
                answer += 1
            elif (sum > n):
                break

    return answer

# 다른 사람 코드
# while문을 한 번 사용한 방법

def solution(n):
    answer, tmp, i, j = 1, 0, 1, 0
    while i < n // 2 + 1:
        tmp += (i + j)
        j += 1
        if tmp >= n:
            if tmp == n:
                answer += 1

            i += 1
            tmp, j = 0, 0

    return answer

