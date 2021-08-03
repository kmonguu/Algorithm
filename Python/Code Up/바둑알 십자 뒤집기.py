#처음 19*19 바둑판을 만들기 위해 2차원 배열을 입력을 받음 
#삼항 연산자를 이용하여 입력받은 좌표값에 따라 1은 0으로, 0은 1로 바꿔서 넣어줌
#돌의 색을 바꾸는 부분에서 삼항 연산자를 생각했지만 코드로 옮기는 것에서 어려웠음

game = [list(map(int, input().split()))for _ in range(19)] #19*19 크기의 바둑판을 만듦
num = int(input())

for i in range(num):
  a, b = map(int, input().split())                         #십자 뒤집기 좌표를 num 횟수만큼 입력받음
  for j in range(19):
    game[a-1][j] = (1 if game[a-1][j] == 0 else 0)         #만약 game[a-1][j] == 0 조건문이 참이면 1, 거짓이면 0을 출력, 가로줄을 바꾼다.
    game [j][b-1] = (1 if game[j][b-1] == 0 else 0)        #game[j][b-1] == 0 조건문으로 세로줄의 0을 1로, 1을 0으로 바꾼다.

for i in range(1, 20):                                     #이중 for문으로 game 배열의 바둑판을 출력해줌
  for j in range(1, 20): 
    print(game[i][j], end=' ') 
    print()
