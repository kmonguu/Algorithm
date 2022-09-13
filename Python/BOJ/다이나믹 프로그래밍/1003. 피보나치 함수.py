# 0 1 1 2 3 5 8 13 .. 과 같은 피보나치 수열은

def fibo(n):
  if (n == 0):
     return 0
    
  elif (n == 1):
      return 1
  else:
      return fibo(n - 1) + fibo(n - 2)
    
# 위와 같은 함수를 통해 구할 수 있다.

# fibo(3)을 오출하면 다음과 같은 일이 일어난다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
# fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
# 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
# fibonacci(0)은 0을 출력하고, 0을 리턴한다.
# fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
# 1은 2번 출력되고, 0은 1번 출력된다.

# fibo(n)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하시오.
