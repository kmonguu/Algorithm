# 피보나치 수는 0과 1로 시작한다. 0 번째 피보나치 수는 0이고, 1 번째 피보나치 수는 1이다.
# 그 다음 2 번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

# 틀린 코드
# 풀이 : 재귀함수를 구현하여 푼 방법 - 시간 초과 발생

def fib(n):
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  else:
    return fib(n-2) + fib(n-1)

n = int(input())
print(fib(n))



# 정답 코드
# 배열에 미리 0과 1에 해당하는 값 0, 1을 넣어두고 2부터 n까지 앞 배열 2개의 합을 구해 배열에 넣어서 n의 값을 구함

n = int(input())
answer = [0, 1]

for _ in range(2, n+1):
  answer.append(answer[-1]+answer[-2])
  
print(answer[n])
