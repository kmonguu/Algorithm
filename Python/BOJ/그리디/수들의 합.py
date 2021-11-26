# 서로 다른 N개의 자연수의 합이 S이다. S를 알 떄, 자연수 N의 최댓값은 얼마인지 출력

# 풀이
# S를 입력받고, 1씩 증가하는 N를 sum에 더했을 때 S보다 커진다면 마지막으로 sum에 더한 N의 갯수를 출력하기 위해 N-1을 출력
# 예를 들어, S가 7이라면 1 + 2 + 3 + 4 마지막 4까지 더하면 S보다 커지게 되므로 1 + 2 + 4를 했을 때 S와 같아지게 된다.
# 결론적으로 서로 다른 자연수의 갯수인 N의 최댓값은 4개에서 -1을 한 3이 출력된다.


# 코드
import sys
input = sys.stdin.readline

S = int(input())
sum = 0                         # 1씩 증가하는 N를 더하는 변수
N = 1

while sum < S:                  # sum이 S보다 작을 때 반복
  N += 1                        # N에 1증가
  sum += N                      # N를 sum에 더해줌
  
print(N-1) 


# 다른 방법 : N이 1부터 1씩 증가하면서 sum에 더해지는 것을 식으로 만들면 N*(N+1)/2 가 된다. 이 식을 활용한 방법으로 문제를 풀 수 있다.
import sys
input = sys.stdin.readline

S = int(input())
N = 1

while N*(N+1)/2 <= S: 
  N += 1
  
print(N-1) 



# 다른 방법 : S가 주어졌을 때 1부터 더해가지 않고 S에서 거꾸로 1씩 빼면서 비교하는 방법으로 풀 수 있다.
S = int(input())

N = 1
while 0 <= S:
   S -= N
   N += 1
  
print(N-2) 
