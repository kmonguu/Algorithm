# 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하고
# 두 수를 곱한 값을 누적하여 더함
# 최종적으로 누적된 값 중 최솟값을 반환

# 내가 푼 코드
# A 배열을 오름차순 정렬, B배열을 내림차순으로 정렬 후, 각 자리의 값을 곱하여 더한 값이 최솟값이 됨

def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse=True)

    return sum([a * b for a, b in zip(A, B)])
