# 첫번 째 줄에 설탕의 무게인 N을 입력받고 3g, 5g 밖에 없는 봉지에 최대한 적은 수의 봉지에 나누어 담아야 한다.
# 만약 3g, 5g 봉지에 나누어 담을 수 없다면 -1을 출력한다.

N = int(input())
count = 0

while N >= 0 :		      # 입력받은 N이 0이상일 때 참
  if N%5 == 0:		      # N이 5의 배수일 경우
    count += (N//5)	    # 봉지의 개수를 세는 count변수에 N에 5를 나눈 몫을 더한다.
    print(count)
    break

  N -= 3			          # 만약 N이 5의 배수가 아닐 경우 N에 3을 뺀다.
  count += 1		        # 3g을 빼주었기 때문에 봉지의 수를 하나 늘려준다.
			                  # 이 과정을 반복하여 마지막에 count 변수를 출력

else:			              # 입력받은 N이 0보다 작을 경우
  print(-1)		          # -1을 출력한다.
  
	
	
# while - else문을 사용하여 문제를 풀 수도 있지만 if - else 문을 사용하여 코드의 가독성을 높일 수 있다.

N = int(input())
count = 0

while N > 0 :
  if N%5 == 0:
    count += (N//5)   
    break

  N -= 3
  count += 1

if N < 0:
  print(-1)
else:
  print(count)

# 다른 풀이) 3x + 5y = N의 식에서 x와 y의 최솟값을 구하는 문제로 간단히 요약할 수 있다. 이 식을 사용하여 다음과 같이 풀이할 수 있다.

N = int(input())
count = 0

for i in range(N//3 + 1):
  for j in range(N//5 + 1):
    if (3 * i + 5 * j) == N:
      print(i + j)
      exit()

print(-1)
