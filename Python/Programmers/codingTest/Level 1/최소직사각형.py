# 지갑의 크기를 정하려고 할 때, 매개 변수로 주어지는 다양한 크기의 명함을 모두 수납할 수 있는 크기여야 한다.
# 모든 명함을 수납할 수 있는 가장 작은 지갑의 크기를 반환

# 내가 푼 코드
# 명함을 적절히 회전시키면 가로가 세로로, 세로가 가로도 될 수 있다.
# 한 명함의 가로와 세로로 주어진 크기를 비교하여 작은 값은 세로로, 큰 값은 가로로 가정하여 다시 정렬하였다.
# 다시 정렬된 명함들은 0번 인덱스엔 작은 값인 세로 크기가, 1번 인덱스엔 큰 값인 가로 크기가 저장되어 있다.
# zip을 사용하여 0번 인덱스, 1번 인덱스 끼리 묶어주었다.
# 그 중 각각 최댓값을 찾아 곱하면 모든 명함을 수용할 수 있는 가장 작은 크기의 지갑 크기가 나온다.

def solution(sizes):
    sizes = [sorted(size) for size in sizes]
    answer = list(map(list, zip(*sizes)))
    return max(answer[0])*max(answer[1])



# 다른 사람 코드
def solution(sizes):
    return max([max(size) for size in sizes]) * max([min(size) for size in sizes])
