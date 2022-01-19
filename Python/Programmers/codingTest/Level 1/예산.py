# 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지 반환

# 내가 푼 코드
# 입출력 예 2의 d = [2,2,3,3], budget = 10 인 경우 가지고 있는 예산으로 모든 부서의 물품을 구매해줄 수 있으므로 신청한 부서의 개수 4가 반환된다.
# 이러한 경우를 위해 크게 조건을 (모든 부서의 신청 물품의 총 금액) <= (예산)인 경우와 아닌 경우로 나누어줍니다.
# 구매해야 할 물품의 총 금액이 예산보다 클 경우, answer이라는 새 배열의 sum(answer) <= budget인 경우 정렬된 d의 값을 작은 값부터 넣습니다.
# 지원되는 부서의 개수를 반환해야 하므로 answer의 길이에서 1을 뺀 값을 반환해줍니다.

def solution(d, budget):
    answer = []
    
    if sum(d) <= budget:
        return len(d)
    else:
        while sum(answer) <= budget:
            d.sort()
            answer.append(d.pop(0))
            
        return len(answer)-1
