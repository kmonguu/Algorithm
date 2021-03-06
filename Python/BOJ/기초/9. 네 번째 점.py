# 좌표의 세 점을 입력하면 직사각형의 네 번째 점의 좌표를 출력
# 직사각형이 마주보는 두 변의 길이가 같다는 특성을 활용하여 직사각형의 4개의 (x, y)좌표엔 같은 수가 2개씩 있다는 점을 이용
# 출력해야 할 네 번째 좌표를 구하기 위해선 입력받은 3개의 (x, y)좌표에서 하나씩만 있는 x, y를 구해 출력하면 된다.


x_list = []                                   # 입력받은 3개의 직사각형의 x좌표를 담기 위한 리스트
y_list = []                                   # 입력받은 3개의 직사각형의 y좌표를 담기 위한 리스트

for _ in range(3):                    
  x, y = map(int, input().split())

  x_list.append(x)                            # 각각의 x좌표를 리스트에 저장
  y_list.append(y)                            # 각각의 y좌표를 리스트에 저장

for i in range(3):                            # 리스트의 인덱스로 사용할 for문
    if x_list.count(x_list[i]) == 1:          # x_list에서 x_list[i] 값이 1개 이면 해당 x좌표 값이 하나가 모자르므로 네 번째 점의 x좌표가 된다. 
      x4 = x_list[i]                          # 해당 x_list[i]의 값을 x4변수에 저장
      
    if y_list.count(y_list[i]) == 1:          # y_list에서 y_list[i]의 값이 1개일 경우
      y4 = y_list[i]                          # y4 변수에 y_list[i]값 저장
      
print(x4, y4)






# 다른 풀이 : xor 연산을 이용한 방법
# xor 연산은 입력받은 수를 이진수로 바꾸었을 때 비교하는 두 수가 서로 같으면 0을 출력, 다르면 1을 출력한다.
# x좌표의 xor연산, y좌표의 xor연산을 통해 나머지 한 점의 좌표를 구할 수 있다.

# 입력받은 좌표값을 리스트로 저장하지 않고 바로 xor 연산하는 방법

x, y = 0, 0
for _ in range(3):
  a, b = map(int, input().split())
  
  x ^= a                                    # 예를 들어, 5가 입력됐다면 이진수로 101, x는 000이므로 xor연산으로 101이 나온다. 이 값을 x에 저장하고 다음 연산을 한다.
  y ^= b
  
print(x, y)
