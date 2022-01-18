# 두 정수 left와 right가 매개변수로 주어졌을 때, left부터 right까지의 모든 수 중에서 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 반환

# 내가 푼 코드
# left와 right사이의 수를 차례대로 순회하며 약수의 개수를 cnt를 증가시키며 구한다.
# 약수의 개수 cnt가 짝수이면 answer배열에 그대로, 홀수개이면 -를 붙여서 배열에 담아준다.
# 배열에 담긴 수의 합을 구하면 된다.

def solution(left, right):    
    answer = []
    for num in range(left, right+1):
        cnt = 0
        for prime in range(1, num+1):
            if num % prime == 0:
                cnt += 1
        answer.append(num) if cnt % 2 == 0 else answer.append(-num)
            
    return sum(answer)
  
  
  
# 다른 사람 코드
# 약수가 홀수개인 모든 정수는 제곱수인 것을 이용하여 left와 right 사이의 정수의 제곱근이 그의 int형과 같다면
# 이 정수는 제곱수로, 약수의 개수가 홀수인 수가 되므로 음수로 바꿔준다.

def solution(left, right):
    return sum([-n if int(n ** 0.5) == n ** 0.5 else n for n in range(left, right+1)])
