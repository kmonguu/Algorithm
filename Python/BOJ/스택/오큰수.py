# 어떤 수열을 입력받고 이 수열의 각각의 원소에 대해 원소 A에 대해 오른쪽에 있으면서 A보다 큰 수 중에서 가장 왼쪽에 있는 수를 오큰수라고 한다.

# 예시
# 예를 들어, 수열 [3, 5, 2, 7]이 있을 때, 
# 첫 번째 원소 3에 대한 오큰수는 오른쪽에 있으면서 3보다는 크고 가장 왼쪽에 있는 5를 의미한다.
# 또 두 번째 원소 5에 대한 오큰수는 7이 되고
# 2에 대한 오큰수도 7이 된다.
# 마지막 원소 7에 대한 오큰수는 존재하지 않으므로 -1을 출력한다.

# 풀이
# 스스로 풀지 못함. 인터넷 참고한 풀이와 코드
# 이중 for문을 사용하여 풀 수도 있지만 시간초과가 나기 때문에 스택으로 풀어야한다.
# stack에는 원소의 값이 아닌 해당 원소의 인덱스를 넣어줘야한다.
# while의 조건문으로 비교하는 수열의 수가 stack[-1]보다 크다면 오큰수가 담겨있는 배열 result에 해당 인덱스의 값을 pop하고 현재 수로 바꿔줌


# 코드
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
result = [-1]*N                                   # 오큰수가 존재하는 않는 경우를 대비해 result 리스트를 N만큼 -1로 초기화


for idx in range(N):                              # 인덱스를 의미하는 idx변수에 범위를 N으로 선언하여 for문으로 반복
  while stack and arr[stack[-1]] < arr[idx]:      # while 반복문으로 stack에 요소가 있으면서 arr[stack[-1]] < arr[idx] 일 때 실행
    result[stack.pop()] = arr[idx]                # result배열에서 stack.pop() 한 인덱스 자리에 arr[idx]를 넣는다.
  stack.append(idx)                               # while문 조건에 해당이 안되거나 while반복이 끝나면 idx를 stack에 append한다.
print(*result)
