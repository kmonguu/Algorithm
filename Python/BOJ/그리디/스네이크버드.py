# 스네이크버드는 과일 하나를 먹으면 길이가 1만큼 늘어납니다.
# 과일들은 지상으로부터 일정 높이를 두고 떨어져 있으며 i (1 ≤ i ≤ N) 번째 과일의 높이는 hi입니다. 
# 스네이크버드는 자신의 길이보다 작거나 같은 높이에 있는 과일들을 먹을 수 있을 때, 스네이크버드의 처음 길이가 L일때 과일들을 먹어 늘릴 수 있는 최대 길이를 출력


# 내가 푼 코드
# 과일이 있는 높이를 heights에 입력받은 후, 오름차순으로 정렬한다.
# for문으로 heights를 돌면서 현재의 스네이크버드의 길이인 l과 비교하여 작거나 같으면 현재 길이에서 +1을 해준다.

n, l = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

for height in heights:
  if height <= l:
    l += 1
print(l)
