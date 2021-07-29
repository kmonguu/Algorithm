#변수 a, b, c를 내장함수 map()을 사용하여 정수형으로 입력받음
#for문을 3중으로 사용하여 a, b, c가 오름차순으로 각각 0부터 a-1, b-1, c-1까지 모든 경우를 출력할 수 있게 한다.
#count를 0으로 초기화하고 모든 경우를 count하여 마지막에 출력한다.

a, b, c = map(int, input().split()) #map 함수를 사용하여 a, b, c를 int형으로 입력받음
count = 0  #경우의 수를 카운트하는 변수 count를 0으로 초기화 

for i in range(0,a): #0부터 a-1까지 첫 번째 for문
  for j in range(0,b): #0부터 b-1까지 두 번째 for문
    for k in range(0,c): #0부터 c-1까지 세 번째 for문
      print('%d %d %d'%(i, j, k)) #모든 경우를 줄을 바꿔 출력
      count = count + 1 #경우의 수의 갯수를 count+1하며 수를 센다.
print(count) 
