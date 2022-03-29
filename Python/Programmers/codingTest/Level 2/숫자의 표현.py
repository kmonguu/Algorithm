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
