# 함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, 함수 D는 첫 번째 함수를 버리는 함수이다.
# 만약, 배열이 비었는데 D를 사용한 경우에는 에러가 발생한다.


# 풀이
# 배열을 입력받을 때, 대괄호와 쉼표를 같이 입력받으므로 정수들은 쉼표로 구분을 하고, 대괄호는 제거되어야 한다.
# 대괄호가 배열의 양쪽 가장자리에 있다는 것을 이용하여 [1:-1]범위만 슬라이싱하여 deque를 만든다.

# 대괄호를 포함하여 배열을 입력받으므로 배열의 정수의 개수인 n이 0이라도 deque의 길이가 1이 된다.
# if문을 사용하여 n이 0인 경우는 배열이 비어있도록 초기화해주어야 한다.

# R이 입력되었을 때 배열에 있는 숫자의 순서을 뒤집는다. 이때 R이 입력될 때마다 뒤집어준다면 시간초과가 발생한다.
# R이 입력되었을 때 매번 뒤집는 것이 아닌 R이 입력되는 횟수를 count하여 뒤집는 횟수가 홀수 번일 때만 뒤집어 주어야 한다.


# 코드
import sys 
input = sys.stdin.readline

from collections import deque

T = int(input())                                        # 테스트케이스
for i in range(T):
  p = input()                                           # 수행할 함수
  n = int(input())                                      # 배열에 들어있는 수의 개수
  numbers = deque(input().strip()[1:-1].split(','))     # 대괄호를 제외하고 [1:-1] 범위로 쉼표로 구분된 정수를 numbers에 deque로 선언 

  if n == 0:                                            # n이 0이라면 배열 안에 들어있는 수가 0개라는 의미이므로
    numbers = []                                        # numbers를 비어있는 배열로 초기화해준다.

  check = True                                          
  cnt = 0                                               # R이 몇 번 입력되었는지 count하기 위해 0으로 초기화

  for in_p in p:
    if in_p == 'R':                                     # p에 있는 요소 in_p가 R이면
      cnt += 1                                          # cnt에 +1

    elif in_p == 'D':                                   # p에 있는 요소가 D인 경우
      if len(numbers) < 1:                              # numbers배열의 길이가 1보다 작다면
        print('error')                                  # numbers배열에서 삭제해줄 데이터가 없으므로 error문을 출력
        check = False                                   # error가 발생한 경우는 출력을 하지 않기 위해 check를 False로 저장
        break

      else:                                             # 에러가 발생하지 않는 경우
        if cnt % 2 == 0:                                # R이 입력된 횟수가 짝수 번 이라면
          numbers.popleft()                             # numbers 배열의 첫 번째 숫자를 뽑아낸다.
        else:                                           # R이 입력된 횟수가 홀수라면
          numbers.pop()                                 # 배열에 저장된 수가 한번 뒤집어졌다는 의미이므로 배열의 가장 뒤에서 숫자를 뽑아낸다.

  if check == True:                                     # check가 True인 경우                                
    if cnt % 2 == 0:                                    # R이 입력된 횟수가 짝수일 때
      print('['+','.join(numbers)+']')                  # 뒤집기에서 변화가 없으므로 numbers 배열을 그대로 출력

    else:                                               # R이 입력된 횟수가 홀수라면
      numbers.reverse()                                 # 배열에 있는 숫자의 순서를 뒤집어주고 출력한다.
      print('['+','.join(numbers)+']')                  
  
