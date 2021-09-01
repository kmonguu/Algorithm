# 자연수 M과 N을 입력받고 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 출력
# M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력

M = int(input())
N = int(input())

sosu = []

for i in range(M, N+1):     # M와 N까지를 범위로 하는 for문
  if 1 < i:                 # 1은 소수가 아니므로 i가 1보다 클 경우를 if문의 조건으로 설정
    check = True            
    for j in range(2, i):   # 1과 자기자신만으로 나누어 떨어지는 수가 소수이므로 나누는 수를 2부터 i까지 변수 j를 선언
      if i%j == 0:          # 만약 i가 j로 나누었을 때 나누어 떨어진다면 1과 자기자신 외에 나누어 떨어지는 수가 있다는 의미이므로 소수가 아님
        check = False       # check를 False로 선언
        break

    if check:               # check가 True인 경우 i는 소수이므로
      sosu.append(i)        # sosu 배열에 추가

if len(sosu) == 0:          # 만약 sosu 배열의 길이가 0이라면 M이상 N이하의 자연수 중 소수가 없는 경우이므로
  print(-1)                 # -1을 출력
  
else:                       # 그 외의 경우
  print(sum(sosu))          # sosu 배열의 요소들의 합을 출력
  print(sosu[0])            # 소수들 중 최솟값을 출력
