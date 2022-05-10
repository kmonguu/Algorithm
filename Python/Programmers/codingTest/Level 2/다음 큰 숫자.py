# 자연수 n이 매개변수로 주어질 때, 아래 조건을 만족하는 n의 다음 큰 숫자를 반환
# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

# 예제
# 78의 다음 큰 숫자는 83입니다.
# 78의 2진수 1001110은 83의 2진수 1010011과 비교하여 조건 1, 2, 3을 모두 만족하기 때문

# 내가 푼 코드
# 파이썬의 내장함수 bin을 활용하여 매개변수 n의 이진수를 구하여 '1'의 갯수를 센다.

def solution(n):
    for num in range(n+1, 1000001):
        if(bin(n)[2:].count('1') == bin(num)[2:].count('1')):
            return num
