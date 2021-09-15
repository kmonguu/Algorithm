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
    
    
    
    
    
# 다른 풀이

N = int(input())
s = sorted([int(input()) for _ in range(N)])  # 리스트 컴프리헨션과 sorted 함수를 이용하여 입력 받은 수 오름차순 정렬
print("\n".join(map(str, s)))                 # s의 모든 요소를 문자로 변환 후 개행문자를 기준으로 1\n2\n3\n4\n5 이렇게 join
    
  
  
  
# 위의 코드를 한 줄로도 나타낼 수 있다.

print("\n".join(map(str, sorted([int(input()) for _ in range(int(input()))]))))




# 입력
5     # 입력받을 수의 갯수
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
