# N 마리의 폰켓몬 중에서 N/2마리를 가져갈 수 있다.
# 폰켓몬의 종류를 모두 다르게 들고 가려고 할 때 가져갈 수 있는 폰켓몬 종류의 개수를 반환

# 내가 푼 코드
# set 함수를 이용하여 중복되지 않은 폰켓몬의 종류를 구하고 그 길이를 nums_set에 저장한다.
# 가져갈 수 있는 폰켓몬의 수(N/2)가 nums_set보다 많다면 종류를 각각 다르게 가져가야 하므로 데려갈 수 있는 폰켓몬의 최댓값은 nums_set이 된다.
# 그 외의 경우에는 가져갈 수 있는 폰켓몬의 수를 반환하면 된다.

def solution(nums):
    nums_set = len(set(nums))
    return nums_set if nums_set < len(nums)/2 else len(nums)/2
        
