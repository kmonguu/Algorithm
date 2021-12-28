# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램


# 풀이
# 입력한 세 수를 배열 안에 오름차순으로 정렬하여 저장한다.
# 정렬한 배열의 요소 중에서 두 번째로 큰 정수를 구하기 위해 배열의 2번째 자리의 수를 출력하면 된다. 


# 코드
import sys
input = sys.stdin.readline

arr = sorted(map(int, input().split()))
print(arr[1])
