# N개의 수가 주어졌을 때, 이 수들을 정렬하여 출력
# 배열을 생성하여 입력한 수를 배열에 담아 정렬한 후 출력했다.

# 코드
N = int(input())
s = []                            # 입력받은 수를 담기위한 배열

for _ in range(N):
  n = int(input())

  s.append(n)                     # 입력받은 수 n을 s변수에 저장
  s = sorted(s)                   # s변수에 있는 값들을 정렬하여 다시 s에 저장
  
for i in s:                       # s배열에 있는 요소를 for문을 이용하여 i에 선언
    print(i)          
    
    
# 입력
5
3
2
4
1

# 출력
1
2
3
4
5
