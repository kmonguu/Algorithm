# 정수 N과 X를 입력받아서 다음 줄에 정수가 N개인 수열 A를 입력 받는다.
# 수열 A에서 X보다 작은 수를 출력한다.

N, X = map(int, input().split())

A = list(map(int, input().split()))
for i in range(N):                    # 입력받은 정수 N까지 범위로 하여 변수 i로 for문을 만든다.
    if A[i]<X:                        # 만약 A 내에 있는 요소들이 X 보다 작을 때 print문으로 넘어가게 한다.
        print(A[i], end=' ')          # X보다 작은 값이 담긴 A를 출력하고 end로 공백을 한칸 띄워 한줄에 출력되도록 한다.
