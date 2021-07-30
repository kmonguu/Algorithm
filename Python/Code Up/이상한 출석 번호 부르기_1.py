#for 반복문 내에 d리스트의 a[i]번째 해당하는 수를 1증가하도록 접근하는 것이 어려웠음

num = int(input())
a = input().split()
d = []               

for i in range(num): #0부터 num-1까지 for문
  a[i] = int(a[i])   #a에 저장되어 있는 값을 순서대로 정수형(int)로 변환하여 다시 저장

for i in range(24):  #0부터 23까지 for문
  d.append(0)        #[0, 0, 0, ..., 0] 과 같이 24개의 정수값을 append를 사용하여 0으로 초기화한다.

for i in range(num): #0부터 num-1까지 for문
  d[a[i]] += 1       #번호를 부를 때마다 그 번호에 대한 카운트를 1증가한다.
                     #예를 들어, n이 3이고 a에 3, 4, 5를 입력한다면 a[1] = 3, a[2] = 4, a[3] = 5가 된다. 이렇게 한번씩 학생들이 불린다면
                     #d[3], d[4], d[5]에 1씩 증가해야 한다.

for i in range(1, 24):
  print(d[i], end=' ')
