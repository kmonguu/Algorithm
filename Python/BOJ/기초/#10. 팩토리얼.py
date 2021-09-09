# 정수 N이 주어졌을 때 N!을 출력하는 프로그램

N = int(input())

def fact(N):                  # 팩토리얼 함수 구현
  if N == 1 or N == 0:        # 입력받은 N이 1이나 0일 경우 
    return 1                  # 1 반환

  else:                       # 그 외의 경우
    return N*fact(N-1)        # N * fact(N-1) 이라는 팩토리얼 점화식을 적용하여 재귀적으로 함수 호출

print(fact(N))                # fact 함수를 호출하여 print로 출력
