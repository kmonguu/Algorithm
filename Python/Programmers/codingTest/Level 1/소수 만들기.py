# 숫자들이 있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 수를 반환

# 풀이
# combinations로 숫자가 중복되지 않도록 하여 조합을 만든 뒤 그 합을 arr에 담는다.
# arr에 담긴 수가 소수인지 판별하여 True 인 것만 개수를 세어 반환한다.

# 코드
from itertools import combinations

def solution(nums):
    arr = []
    for i in combinations(nums,3):
        arr.append(sum(i))
    
    cnt = 0
    for a in arr:
        if 1 < a:
            check = True
            for b in range(2, int(a ** 0.5)+1):
                if a % b == 0:
                    check = False
            if check:
                cnt += 1
    return cnt
