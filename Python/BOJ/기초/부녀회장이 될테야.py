# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야한다는 조건인 아파트가 있다.
# k층에 n호에는 몇 명이 살고 있는지 출력, 0층의 i호에는 i명이 살고 있다.
# 이 문제의 규칙은 0층에는 1호부터 i호까지 1, 2, 3, 4, 5,... , i명이 살고 있고
# 1층엔 1, 3, 6, 10, 15,  ... 2층엔 1, 4, 10, 20, 35, ... 3층엔 1, 5, 15, 35, 70, ... 이라는 규칙이 만들어진다.


# 1. 2차원 배열로 푸는 방법
# 2차원 리스트를 생성하고 초기값을 전부 0으로 한다. 0층은 i호에 i명이 살고 있으므로 0층은 채워준다.
# 2차원 배열의 k층의 n호 규칙을 살펴보면 apart[k][n] = apart[k][n-1] + apart[k-1][n]이라는 식이 세워지고 이 식을 이용하여 문제를 풀 수 있다.

T = int(input())

for _ in range(T):
  k = int(input())
  n = int(input())

  apart= [[0] * (n+1) for _ in range(k+1)]          # 리스트 컴프리헨션을 사용하여 2차원 리스트를 만든 뒤 모든 요소를 0으로 설정
  for i in range(n+1):
    apart[0][i] = i                                 # for문을 사용해 0층의 i호수에 0부터 n까지의 값을 넣어준다.

  for i in range(1, k+1):
    for j in range(1, n+1):
      apart[i][j] = apart[i][j-1] + apart[i-1][j]   # for문 변수 i와 j로 층마다 호수의 사람들 더하여 배열에 저장하는 것을 반복

  print(apart[k][n])
  
  
# 2. 1차원 배열로 푸는 방법
#  1차원 배열을 이용하여 푸는 경우 i층일 때 apart[j] = apart[j] + apart[j - 1] 이라는 식을 세울 수 있다.

T = int(input())

for _ in range(T):
  k = int(input())
  n = int(input())

  apart = [i for i in range(n+1)]
  for i in range(1, k+1):
    for j in range(1, n+1):
      apart[j] = apart[j-1] + apart[j]
  print(apart[n])
  
