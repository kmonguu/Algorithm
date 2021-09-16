# N을 홀수라고 가정했을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성
# 1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 2. 중앙값 : N개의 수들을 오름차순으로 정렬했을 때 중앙에 위치하는 값
# 3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값 (만약 여러 개일 경우 최빈값 중 두 번째로 작은 값)
# 4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

# 최빈값을 구하기 위해 데이터의 개수를 셀 때, 파이썬에서 제공하는 collections 모듈의 Counter 클래스를 이용
# 데이터가 들어있는 num 배열의 숫자들을 예를 들어, [2, 3, 3, 4] 배열이 있다면 {2: 1, 3: 2, 4: 1}의 딕셔너리 형태로 수를 세어 줌


from collections import Counter                                         # collections 모듈의 Counter 클래스
import sys
input = sys.stdin.readline

N = int(input())
num = sorted([int(input()) for _ in range(N)])                          # num 배열 안에 수를 입력받고 정렬하여 저장

print(round(sum(num)/N))                                                # 산술평균 ( 반올림을 한 값을 출력하기 위해 round 사용)
print(num[N//2])                                                        # 중앙값

counter = Counter(num)
result = sorted(counter.items(), key=lambda x : (-x[1], x[0]))          # counter.items()를 통해 딕셔너리 형태를 (key, value)의 형태로 변환
                                                                        # lambda 식을 보면 (key, value)에서 value를 내림차순 정렬, key를 오름차순 정렬시키겠다는 의미

if len(result) != 1:                                                    # 최빈값 배열이 1이 아닐 경우 (배열이 1개 이상일 때)
  if result[0][1] == result[1][1]:                                      # 최빈값이 여러 개인 경우
    print(result[1][0])                                                 # 최빈값 배열에서 두 번째로 작은 값을 출력

  else:
    print(result[0][0])                                                 # 최빈값
else:
  print(result[0][0])

print(max(num)-min(num))                                                # 범위 (오름차순으로 정렬된 num 배열의 최댓값고 최솟값의 차를 구함)




# 다른 풀이
import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())
num = sorted([int(input()) for _ in range(N)])

print(round(sum(num)/N))
print(num[N//2])
                                                                  # Counter 모듈의 most_common 메소드는 카운팅된 딕셔너리에서 카운팅 횟수가 가장 많은 순으로 정렬해줌
                                                                  
                                                                  # 정렬된 num에서 Counter 모듈을 이용하여 num 배열에 입력된 수의 횟수를 세고,
result = Counter(num).most_common()                               #  most_common() 메소드를 이용하여 횟수가 많은 순으로 정렬하여 result에 
if len(result) != 1 and result[0][1] == result[1][1]:             # 최빈값이 여러개이면
    print(result[1][0])                                           # 최빈값 중 두번째로 작은값 출력
else:
  print(result[0][0])                                             # 최빈값이 1개이면 바로 출력

print(num[-1] - num[0])                                           # num은 이미 정렬되어 있으므로 max, min 함수를 사용하지 않고 마지막 요소에서 첫번째 요소를 빼면 됨
