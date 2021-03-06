# 땅따먹기 게임의 땅은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있다.
# 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 한다. (한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있다.)
# 마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최댓값을 반환 - DP(Dynamic Programming) 알고리즘

# 내가 푼 코드
# j가 방문했던 열을 연속해서 밟는 것을 막기 위해 인덱스 슬라이싱을 사용하고 j를 기준으로 앞, 뒤 값 중 가장 큰 값을 구함
# 구한 값들의 합을 반환

def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0]): 
             land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
                               
    return max(land[len(land)-1])
