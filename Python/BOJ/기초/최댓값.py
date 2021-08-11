# 9개의 서로 다른 자연수를 입력하고 출력의 첫째 줄에 최댓값을 출력하고, 둘째 값에 최댓값의 위치를 출력하는 문제
# 최댓값은 파이썬 내장함수 max()를 활용, 최댓값의 위치는 index()를 활용했다.

a = []                      
for i in range(9):          # 9개의 수를 for문으로 입력받음
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)    # index 함수의 순서는 0번째부터 시작하기 떄문에 1을 더해주었다.

# 9개의 숫자를 입력받기 위한 리스트를 만들기 위해 리스트 컴프리헨션으로 작성할 수 있다.
a = [int(input()) for _in range(9)]

