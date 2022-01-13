# 1부터 45까지의 숫자 중에서 6개를 찍어서 맞히는 복권을 구매했지만, 일부 번호를 알아볼 수 없게 되어 0으로 표시하였다.
# 이때, 당첨 번호 발표 후, 이 복권으로 가능했던 최고 순위와 최저 순위를 반환

# 나의 코드
# 구매한 복권 중 알아볼 수 없게 된 복권이 있을 수도 없을 수도 있으므로 우선 알아볼 수 있는 번호 중 당첨 번호와 일치하는 개수를 cnt로 구합니다.
# cnt는 0으로 대체된 번호를 제외하므로 현재 복권에서 나올 수 있는 최저등수가 됩니다.
# 0으로 처리한 알아볼 수 없는 번호가 당첨번호와 일치한 경우, 나의 복권에서 0의 개수를 구하여 cnt와 더한 값이 복권 최고 등수가 되므로 answer에 저장합니다.
# 최고 등수 answer의 value 값과 최저 등수 cnt의 value값을 result배열에 담아 반환

def solution(lottos, win_nums):
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1

    answer = 0
    if lottos.count(0):
        answer = cnt + lottos.count(0)    
    else:
        answer = cnt

    result = []
    result.append({6:1, 5:2, 4:3, 3:4, 2:5}.get(answer, 6))
    result.append({6:1, 5:2, 4:3, 3:4, 2:5}.get(cnt, 6))

    return result
  
  
  
# 다른 사람 코드
# 등수를 미리 배열에 담고 나의 복권에서 0의 개수와 당첨 번호와 일치한 번호가 몇 개인지 구한 값을 인덱스로 사용하여 간단하게 등수를 구했다.

def solution(lottos, win_nums):

  rank=[6,6,5,4,3,2,1]

  cnt = lottos.count(0)
  ans = 0
  for i in win_nums:
      if i in lottos:
          answer += 1
  return rank[cnt + answer],rank[answer]



# 교집합을 사용한 방법

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    answer = len(set(win_nums) & set(lottos))
    return [rank[answer + lottos.count(0)], rank[answer]]

