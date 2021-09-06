# 첫째 줄엔 테스트 케이스의 수, 둘째 줄부터 학생의 수와 이어서 같은 줄에 N명의 점수를 입력한다.
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력하는 문제
# 첫 코드 제출 때 score 인덱싱 [1:]을 해줬어야 했는데 입력받은 모든 값을 for 문 조건으로 넣어서 틀림

C = int(input())

for _ in range(C):
    score = list(map(int, input().split()))
    a = sum(score[1:])/score[0]               # 입력받은 점수 리스트를 1번 배열부터 배열끝까지를 더한 값을 score[0]에 입력된 학생 수로 나누어 평균을 구한 뒤 a에 저장한다.

    count = 0                                 # 점수가 평균을 넘는 학생 수를 구하기 위해 count변수를 0으로 초기화한다.
    for i in score[1:]:
        if i > a:                             # if문을 사용하여 for문 변수 i가 평균점수 a보다 크다면
            count += 1                        # count에 1을 증가 후 더해준다.

    rate = (count/score[0])*100               # 평균점수를 넘는 학생의 비율을 구하기 위해 rate변수에 (평균점수보다 큰 점수를 가진 학생/학생 수)*100을 계산한 값을 저장한다.
    print("{:.3f}%".format(rate))             # format을 활용하여 rate 변수에 저장된 값을 소수점 셋째 자리까지 출력하도록 한다.

    
# 위 코드에서 count변수를 0으로 초기화하고 for 구문을 다음과 같이 한 줄로 나타낼 수 있다.
count = sum([1 for i in score[1:] if i > a])
