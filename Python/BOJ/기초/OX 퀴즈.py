# OX 퀴즈를 했을 때 점수를 계산하는 방법은 연속한 O의 개수를 세다가 X를 만나면 초기화가 되고 다시 1부터 세기 시작한다.
# 예를 들어, OOXXOXXOOO의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# for문과 if문을 사용하여 입력받은 문자열 N에서 O라면 count로 점수를 1씩 증가시키며 더했고 
# 만약 X가 나온다면 점수를 0으로 초기화시켜 다시 시작하도록 했다.
# 이 문제의 포인트인 X를 만났을 때 초기화하는 방법을 미쳐 생각하지 못해 풀이 방법을 생각하는 것에서 시간이 오래걸렸다.


C = int(input())

for _ in range(C):
    N = input()
    count = 0  
    result = 0

    for j in N:
        if j == "X":      # 만약 for문 변수 j가 "X"를 만난다면 count를 0으로 초기화
            count = 0     # 다시 그 다음 "O"를 만날 때 다시 1부터 count를 셀 수 있도록 함
            continue      

        count += 1        # X가 아닌 "O"를 만난다면 count에 1을 증가시키고 값을 count에 저장한다.
        result += count   # 점수계산이 끝난 결과를 result에 저장
    print(result)
