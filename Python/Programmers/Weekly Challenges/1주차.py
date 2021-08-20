# 놀이기구의 이용료가 타는 횟수가 n회라면 이용료도 n배가 된다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 출력

def solution(price, money, count): # price : 놀이기구의 이용료, money : 처음 가지고 있던 돈, count : 놀이기구 이용 횟수
    sum = 0
    m = 0
    for i in range(1, count+1):    # 놀이기구를 타는 횟수만큼 for문 변수 i에 1부터 count+1까지 저장
        sum += (i*price)           # 이용료의 총액을 구하기 위해 놀이기구 타는 횟수 i에 요금을 곱한 값을 sum변수에 저장
    m = money - sum                # 처음 가지고 있던 돈 money에서 놀이기구 이용료 총액을 뺀 잔돈을 변수 m에 저장
    
    if money < sum:                # 만약 가지고 있던 돈이 이용료보다 작을 경우
        return abs(m)              # 돈이 모자라므로 - 값이 나오기 때문에 절대값을 반환하기 위해 abs 함수를 사용
    else:               
        return 0                   # 돈이 모자라지 않을 경우 0을 반환
      
