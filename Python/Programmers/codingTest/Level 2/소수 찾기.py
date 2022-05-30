# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 반환

# 입출력 예
# numbers = "17" 이라고 할 때, [1, 7]로는 소수 [7, 17, 71]을 만들 수 있기 때문에 3이 반환된다.

# 내가 푼 코드
from itertools import permutations

def solution(numbers):
    number = []
    for i in range(1, len(numbers) + 1):
        number += list(permutations(numbers, i))
        
    answer = set([int(''.join(num)) for num in number])
    
    result = 0
    for a in answer:
        cnt = 0
        for i in range(2, int(a**0.5)+1):
            if a % i == 0:
                cnt += 1
                
        if a != 0 and a != 1 and cnt == 0:
            result += 1
                
                
    return result
