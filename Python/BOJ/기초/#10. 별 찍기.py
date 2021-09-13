# 입력받은 N이 3의 거듭제곱이라고 할 때 재귀적인 패턴으로 별을 출력하는 문제이다.
# 이 패턴은 가운데 공백이 있고 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.


N = int(input())

def star(N):                                          # 재귀함수 구현
  global stars                                        # 별을 저장하는 stars 전역변수 선언
  
  if N == 3:                                          # 만약에 N이 3인 경우 가운데를 제외한 가장자리에 별이 찍히므로
    stars[0][:3] = stars[2][:3] = [True]*3            # 2차원 배열을 이용하여 첫 번째 줄과 세 번째 줄에 별을 채운다.
    stars[1][:3] = [True, False, True]                # 두 번째 줄은 '* *'와 같이 가운데 공백을 만들어야 하므로 가운데 False
    return

  a = N//3                                            # N이 3의 몇 제곱인지 구하기 위해 나눈 몫을 a에 저장
  star(N//3)                                          # 재귀함수 호출
  for i in range(3):                                  # 3X3 정사각형을 중첩 for문을 이용하여 생성
    for j in range(3):
      if i == 1 and j == 1:                           # i가 가로 두 번째 줄에서 j가 세로 두 번째줄에 위치한 가운데자리는 공백이므로
        continue                                      # continue

      for z in range(a):                              # 그 외의 경우 변수 z에 N을 나눈 몫이 담긴 a를 선언
        stars[a*i+z][a*j:a*(j+1)] = stars[z][:a]      # 별을 찍기 위해 공백을 제외한 가장자리의 위치를 구함

stars = [['' for x in range(N)] for y in range(N)]    # stars에 N x N 크기의 빈 배열을 생성
star(N)                                               # 재귀함수 실행

for i in stars:
  for j in i:
    if j:
      print('*', end='')
    else:
      print(' ', end='')
  print()
