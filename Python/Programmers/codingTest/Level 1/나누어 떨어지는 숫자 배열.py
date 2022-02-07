# array의 각 요소 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환, 만약 나누어 떨어지는 요소가 하나도 없다면 -1을 반환

# 내가 푼 코드

def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    return answer if answer else [-1]
