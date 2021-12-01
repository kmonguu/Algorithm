# 문서를 검색하는 함수는 어떤 단어가 총 몇 번 등장하는 지 count하려고 한다.
# 이 함수는 단어를 중복적으로 세면 안된다.

# 풀이
# abababa라는 문서가 있고, 그리고 이 문서에서 찾으려는 단어가 ababa 일 때,
# 이 단어를 0번과 2번에서 찾을 수 있다. 하지만 동시에 0번과 2번에서 단어를 찾아 count할 수 없으므로 1이 출력된다.
# 문서 S와 찾으려는 단어 Word를 입력받고 S에 Word가 포함된 횟수를 구하면 된다.

# 코드
S = input()
Word = input()

print(S.count(Word))





# 다른 풀이
# startswith 메소드 : 
# s = s[len(word):] : 문자열 s에서 word 길이만큼만 잘라내고(슬라이싱) 나머지 문자열을 다시 s에 저장

s = input()
word = input()

result = 0
while s:
  if s.startswith(word):        # s가 word로 시작하면 true, 아니면 false를 반환한다.
    result += 1                 # s에 word가 포함된 횟수를 count하기 위해 +1
    s = s[len(word):]           # s에서 word의 길이만큼 슬라이싱으로 잘라내고 난 나머지를 다시 s에 저장한다. 
    continue
  
  s = s[1:]

print(result)
