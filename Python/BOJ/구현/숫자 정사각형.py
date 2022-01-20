# NxM 크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다.
# 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오.

# 예시
# 3 5
# 42101
# 22100
# 22101
# 가 주어진다면 꼭짓점의 수가 1로 모두 같은 넓이가 9인 정사각형이 가장 크기 때문에 9가 출력된다.


# 풀이
# for문을 사용하여 정사각형이면서 꼭짓점의 크기가 같은 경우를 모두 찾아 answer에 갱신하는 방법으로 풀었다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
answer = 0

for i in range(n):
  for j in range(m):
    for z in range(min(n, m)):                                                  # 행과 열 중 더 작은 값을 기준으로 정사각형 탐색
      if i + z < n and j + z < m:                                               # 주어진 인덱스 벗어나지 않았다면
        if board[i][j] == board[i][j+z] == board[i+z][j] == board[i+z][j+z]:    # 꼭짓점의 숫자가 모두 같은지 확인
          if answer < z:                                                        # 현재 answer에 저장된 값이 정사각형 한 변의 길이가 되는 z보다 작다면 
            answer = z                                                          # answer에 z를 저장하여 더 큰 값으로 갱신해준다.

print((answer+1)**2)


