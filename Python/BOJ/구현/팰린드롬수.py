# 어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어를 팰린드롬이라고 한다.
# 121, 12421 과 같은 수도 팰린드롬수라고 할 때, 어떤 수가 주어졌을 때 이 수가 팰린드롬 수라면 'yes'를 아니면 'no'를 출력

# 실패 코드
# 처음 수를 문자열로 받아서 리스트로 만들고 가운데 수를 기준으로 양쪽의 수가 같은지 아닌지 비교하는 것으로 접근했다.

import sys
input = sys.stdin.readline

while True:
  num = list(map(str, input().strip()))
  if num[0] == '0': break  
  print('yes' if num[: len(num)//2 ] == sorted(num[len(num)//2 +1 :]) else 'no')
  
  
# 내가 푼 코드
# 팰린드롬 수라면 입력받은 수와 그 수를 뒤집었을 때 값이 같다는 것을 알고 간단하게 풀 수 있었다.

import sys
input = sys.stdin.readline

while True:
  num = list(map(str, input().strip()))
  if num[0] == '0': break  
  print('yes' if num == num[::-1] else 'no')
