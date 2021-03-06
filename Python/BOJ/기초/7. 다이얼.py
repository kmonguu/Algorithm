# 다이얼 전화기에서 전화를 걸 때 알파벳 대문자로 된 문자를 입력하면 이 단어에 맞는 번호로 전화를 걸기 위해 필요한 최소 시간을 구하는 문제
# 숫자에 해당하는 알파벳을 3개씩 모아 하나의 문자열로 만들고 이 문자열들을 리스트에 저장했다.
# 이후 for문을 이용해서 문자열과 알파벳을 for문 변수에 각각 저장하고 입력받은 문자열과 if문으로 비교하는 방법으로 풀었다.

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

time = 0

for i in dial:                    # dial 리스트의 요소를 i에 저장
  for j in i:                     # i에 담긴 문자열들을 각각의 알파벳으로 분리하여 j에 저장
    for k in word:                # 입력받은 단어 word의 각각의 알파벳 요소를 k에 저장
      if j == k:                  # 변수 j에 저장된 알파벳들과 변수 k에 저장된 알파벳을 서로 비교 후 같을 경우
        time += dial.index(i) + 3 # dial 리스트 안에서 변수 j에 저장된 알파벳이 해당하는 변수 i의 위치를 index 함수를 이용하여 찾고
                                  # 다이얼에서 숫자 1을 누르는데 2초가 걸리고 이후에 1초씩 걸리므로 총 3초를 time에 더해준다.

print(time)


# 2중 for문을 사용한 입력받은 단어 word의 알파벳이 dial 리스트 안에 있는지 확인하여 푸는 방법
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

time = 0
for w in word:                    # 입력받은 단어 word의 요소를 for문 변수 w에 저장
  for i in range(8):              # dial에 담긴 문자열의 갯수 8을 for문의 범위로 하여 for문 변수 i선언
    if w in dial[i]:              # if문을 사용하여 dial 리스트에 for문 변수 i를 이용하여 입력받은 단어의 요소 w가 dial 리스트에 속해있는 경우
      time += (i + 3)             # 전화를 걸 때 걸리는 시간 총 3초를 더하여 time 변수에 저장

print(time)
