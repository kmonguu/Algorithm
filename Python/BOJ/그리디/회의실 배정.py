# N개의 회의를 하나의 회의실에서 해야할 때, 각 회의는 시작시간과 끝시간이 주어져 있다.
# 각 회의가 겹치지 않게 하면서 회의실을 사용하는 회의의 최대 개수를 출력


# 풀이
# 최대한 많은 회의를 하기 위해서는 시작시간이 아닌 끝시간을 기준으로 정렬을 한다.
# 하지만 회의 중 끝시간이 같은 경우를 대비하여 끝시간이 같은 경우 시작시간을 기준으로 정렬한다.



# 코드
import sys
input = sys.stdin.readline

meeting = []                                            # 회의의 시작시간과 끝시간을 저장하는 배열
for _ in range(int(input())):
  meeting.append(list(map(int, input().split())))
meeting.sort(key=lambda x: (x[1], x[0]))                # 람다식을 활용하여 끝시간을 기준으로 정렬한 다음 시작시간을 기준으로 정렬한다.


cnt = 1                                                 # 회의의 개수를 카운트하는 변수를 1로 초기화해둔다.
time_end = meeting[0][1]                                # 회의 끝나는 시간을 time_end라는 변수를 두고 정렬 후 첫 요소의 끝시간을 저장한다.
for idx in range(1,len(meeting)):
  if time_end <= meeting[idx][0]:                       # 앞 회의가 끝나야 다음 회의의 시작시간에 회의를 시작하므로 다음 회의의 시작시간이 time_end보다 같거나 크다면
    cnt += 1                                            # 1 카운트하고
    time_end = meeting[idx][1]                          # 다시 time_end에 다음 회의의 끝시간을 저장한다.
print(cnt)
