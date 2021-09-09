# 삼각형의 세변의 길이를 입력받고 이 삼각형이 직각삼각형이면 'right'를 출력, 아니라면 'wrong'을 출력
# 입력받는 세변의 길이가 항상 오름차순으로 입력되는 것이 아니므로 정렬이 필요
# 오름차순으로 정렬하게 되면 리스트 가장 끝에 오는 길이가 대각선의 길이가 된다.
# 다시 말해, 앞 2개의 길이를 각각 제곱하여 더하면 세 번째 자리에 위치한 대각선의 제곱이 되는 것을 이용해 문제를 품


import sys
input = sys.stdin.readline

while True:
  pita = list(map(int, input().split()))                        # 세변의 길이를 리스트 형태로 입력받음

  if sum(pita) == 0:                                            # 입력 반복이 세변의 길이로 모두 0이 입력되면 종료되도록 함
    break                                                       # and연산자를 사용하여 pita[0] == 0 and pita[1] == 0 ... 으로 할 수 있지만 sum을 사용하여 코드의 길이를 줄임
  
  pita = sorted(pita)                                           # pita 리스트를 오름차순으로 정렬한 뒤 다시 pita에 저장
  if ((pita[0] ** 2) + (pita[1] ** 2)) ** 0.5 == pita[2]:       # 리스트의 첫 번째자리와 두 번째 자리의 길이를 제곱하여 더한 값의 제곱근이 대각선의 길이와 같다면
    print('right')                                              # 직각삼각형이므로 "right"를 출력
  else:
    print('wrong')                                              # 아니라면 "wrong"을 출력

    

    
# 다른 풀이
# 세 변의 길이는 양의 정수이기 때문에 내장함수 sum을 사용하지 않고 첫 번째 요소의 값이 0이 아닌지만 확인하면 됌

import sys
input = sys.stdin.readline

while True:
  pita = sorted(map(int, input().split()))                      # 입력 받으면서 바로 오름차순정렬
  if pita[0] == 0:                                              # 첫 번째 요소의 값이 0이면 break
    break
  
  if ((pita[0] ** 2) + (pita[1] ** 2)) == pita[2] ** 2:         # 피타고라스의 정리
    print('right')
  else:
    print('wrong')
