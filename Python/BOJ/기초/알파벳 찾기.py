# 입력한 단어의 각각의 알파벳에 대해서 a부터 z까지의 알파벳이 처음 등장하는 위치를 출력하는 문제
# 아스키코드의 숫자 범위 이용
# 파이썬 내장함수 find()를 활용하여 a ~ z 알파벳이 입력한 단어에 포함되지 않으면 -1을 출력하도록 했다.

S = input()

alphabet = list(range(97, 123))     # 아스키코드의 숫자 범위(a=97, z=122) 로 리스트를 생성 후 alphabet변수에 저장
for i in alphabet:                  # alphabet 리스트의 각각의 요소를 for문 변수 i에 차례로 대입한다.
  print(S.find(chr(i)), end= ' ')   # chr 함수를 사용하여 아스키코드에 해당하는 숫자를 문자열로 변환 후 find 함수로 입력받은 문자열 S안에서 문자를 찾아 위치를 출력 
  
  
# list를 생성하지 않고 푸는 방법
for alphabet in range(ord("a"), ord("z") + 1):  # ord를 사용하여 특정한 문자 a와 z를 아스키 코드로 변환하여 for문을 범위만큼 반복합니다.
  print(S.find(chr(alphabet)), end=' ')         # 변수 alphabet에 저장된 아스키 코드를 chr을 이용하여 문자로 변환하고 문자열 S안에서 문자를 찾아 출력합니ㅏㄷ.
  
  
# find 함수와 index 함수
# find 함수는 문자열에서 사용가능하고 찾는 문자가 문자열 안에 포함되지 않으면 -1을 출력
# index 함수는 리스트, 튜플에도 사용가능하며 찾는 문자가 문자열 안에 없다면 에러 발생
