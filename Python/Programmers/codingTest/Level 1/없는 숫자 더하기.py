# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어질 때, numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 반환

# 내가 푼 코드
# 1부터 9까지가 들어있는 배열을 만들고 for문으로 순회하여 numbers배열에 있는지 확인하고 없는 숫자들의 합을 반환한다.

def solution(numbers):
    return sum([i for i in [1,2,3,4,5,6,7,8,9,0] if i not in numbers])
  
  
  
# 다른 사람 코드
# 없는 숫자들의 합을 반환하는 문제이므로 0부터 9까지의 합인 45에서 numbers배열의 합의 차를 반환하면 된다.

def solution(numbers):    
    return 45 - sum(numbers)



# set을 이용해 차집합으로 푼 방법

def solution(numbers):
    return sum(set(range(0, 10)) - set(numbers))
