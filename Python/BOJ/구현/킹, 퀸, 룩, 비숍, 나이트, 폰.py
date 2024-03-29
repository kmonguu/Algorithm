# 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.
# 흰색 피스의 개수가 주어졌을 때, 몇 개를 더하거나 빼야 올바른 세트가 되는지 구하는 프로그램을 작성하는 문제

# 예제
# 입력에서 주어진 순서대로 몇 개의 피스를 더하거나 빼야 되는지를 출력한다. 
# 만약, 수가 양수라면 그 개수 만큼 피스를 더해야 하는 것이고, 음수라면 제거한다.

# 입력
# 0 1 2 2 2 7

# 출력
# 1 0 0 0 0 1

# 내 코드

origin_chess_num = [1, 1, 2, 2, 2, 8]

current_chess_num = list(map(int, input().split()))

for idx in range(6):
  print(origin_chess_num[idx]-current_chess_num[idx], end=' ')
