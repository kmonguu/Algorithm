# 피보나치 수는 0과 1로 시작하고 그 다음 번째부터는 바로 앞 두 피보나치 수의 합이 된다.
# 식으로는 f(n) = f(n-1) + f(n-2) 가 되는 것을 이용하여 문제를 풀었다.


n = int(input())

def pibo(n):                        # 피보나치 함수 구현
  if n==0:                          # n의 입력으로 0이 들어오면 
    return 0                        # 0을 반환
  elif n==1:                        # 1이 입력되면
    return 1                        # 1을 반환
  
  else:                             
    return pibo(n-1) + pibo(n-2)    # 피보나치 수를 구하기 위해 pibo 함수를 재귀적으로 호출

print(pibo(n))
