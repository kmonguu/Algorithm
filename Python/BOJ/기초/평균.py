# 시험 본 과목의 점수 중 가장 큰 수를 토대로 새로운 평균을 출력하는 문제이다.
# 예를 들어, 3과목 중 최고점이 70이고, 수학점수가 50점이라면 수학점수는 50/70*100으로 계산하여 새로운 평균은 71.43이 된다.
# 새로운 평균을 계산하는 식을 이해하는 것에 시간이 좀 걸렸지만 이해 후 문제푸는 것은 간단했음


num = int(input())                        # 과목 수
score = list(map(int, input().split()))   # 과목 수만큼 과목의 점수를 입력

M = score[0]
sum = 0

for i in range(num):                      # for문을 이용하여 num까지 범위를 잡고
    if M < score[i]:                      # if문으로 입력받은 점수 중 최댓값을 찾는다.
        M = score[i]

for i in range(num):                      # for문을 이용하여 시험점수를 하나씩 꺼내면서
    score[i] = score[i]/M*100             # (입력받은 점수/최고 점수*100)식으로 새로운 점수를 구한 뒤 score[] 리스트에 저장한다.
    sum += score[i]                       # 새로운 점수들의 평균을 구하기 위해 더한 값을 sum에 저장

result = sum/num                          # 점수를 더한 합을 과목 수로 나누어 result라는 평균을 구함
print(result)
