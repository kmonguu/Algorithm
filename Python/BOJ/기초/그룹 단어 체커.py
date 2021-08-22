# 첫 줄에 입력 받은 단어의 갯수를 입력하고 개수만큼 단어를 입력한다. 이 때 입력 받은 단어 중 그룹 단어의 개수를 출력하는 문제
# 그룹 단어는 단어에 존재하는 각 알파벳이 연속해서 나타나는 경우를 말한다. 
# 예를 들어, ccazzb는 그룹단어이고 abba는 a가 연속해서 나오지 않았으므로 그룹 단어가 아니다.
# 그룹 단어이면 True, 그룹 단어가 아니면 False를 줘서 True의 개수를 세어 출력했다.

num = int(input())

count = 0                # 그룹 단어의 개수를 체크
check = True             # check에 True를 저장하고 그룹 단어일 경우 사용한다.     

for _ in range(num):
  word = input()

  w = []
  for i in word:         # 입력 받은 단어의 요소를 변수 i에 저장
    if w and w[-1] == i: # w 배열에 요소가 있고 w배열의 마지막 요소가 i와 같을 경우
      continue      

    if i in w:           # w 배열 안에 for문 변수 i가 있을 경우 
      count = False      # 해당 단어는 그룹 단어가 아니므로 count에 False를 저장
      break              # 그룹 단어가 아닐 경우 불필요한 연산을 막기 위해 break문 사용
      
    w.append(i)          # w 배열 안에 변수 i가 없다면 w 배열 안에 변수 i를 담는다.
    
  if check:              # check가 True일 경우
    count += 1           # count에 1을 더하고
print(count)             # count를 출력하여 그룹 단어 개수를 알 수 있다.
