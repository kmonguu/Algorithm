# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 문제
# 예를 들어, A = 9223372036854775807, B = 9223372036854775808 일 때 결과를 출력할 수 있어야한다.

import sys                                       # sys 모듈 사용

A, B = map(int, sys.stdin.readline().split())
print(A+B)


# 다른 풀이) 내장 함수 sum을 사용하여 푸는 
print(sum(map(int, input().split())))            
