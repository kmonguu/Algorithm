# 땅따먹기 게임의 땅은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있다.
# 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 한다. (한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있다.)
# 마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최댓값을 반환


# 내가 푼 코드

def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0]): 
             land[i][j] += max(land[i-1][:j] + land[i-1][j+1:]
                               
    return max(land[len(land)-1])
            
