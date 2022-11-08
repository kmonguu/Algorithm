# 등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 반환

# 예제
# [1, 2, 3, 4] -> 	5
# 공차가 1인 등차수열이므로 마지막 값 4에 1을 더한 5를 반환

# [2, 4, 8] -> 	16
# 공비가 2인 등비수열이므로 마지막 값 8에 2를 곱한 16을 반환

# 내가 푼 코드 

def solution(common):
    
    if common[-1]-common[-2] == common[-2]-common[-3]:
        return common[-1] + (common[-1]-common[-2])
    
    else:
        return common[-1] * (common[-1]/common[-2]) 
