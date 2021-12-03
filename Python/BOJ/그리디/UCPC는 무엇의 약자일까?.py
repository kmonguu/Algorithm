# 입력으로 들어온 문자열을 적절히 축약해서 'UCPC'로 만들 수 있는지 확인하는 문제
# 문자열을 비교할 때는 대소문자를 구분해 정확히 비교한다. 
# 예를 들어, 'UCPC'와 'ucpc'는 다른 문자열이다.


# 처음 생각한 나의 풀이
# 문자열을 받아서 공백을 기준으로 자른다.
# 자른 문자열의 첫 번째 문자가 'U', 'C', 'P'. 'C' 중 하나이면 새로운 배열에 담는다.
# 최종적으로 새로운 배열에 담긴 문자가 'UCPC'와 같으면 'I love UCPC', 아니라면 'I hate UCPC'를 출력하도록 했다.

# 틀린 이유
# 반례로 'UUUCCCCPPPCCC'가 들어오면 이대로 문자열에 담기는데, 순서를 유지하며 중복되는 문자를 삭제할 수 없었음

# 코드
S = input().split(' ')
result = []

for i in S:
  arr = str(i[0])
  
  if arr.isupper() == True:
    result.append(arr)

if ''.join(result) == 'UCPC':
  print('I love UCPC')

else:
  print('I hate UCPC')
  
  
  
  

# 새로운 풀이
# word 배열에 ['U', 'C', 'P', 'C']를 넣어두고 각각의 요소가 문자열 s에 있는지 확인하고, 있다면 arr 배열에 넣어주도록 했다.
# 이렇게 되면 확인했던 문자열을 다시 비교하고 넘어가는데 이러면 중복체킹이 된다.
# 이를 방지하기 위해 s문자열 안에서 word 요소를 찾았다면 arr 배열에 넣고 그 다음 요소부터 확인되도록 s에 담기는 요소를 슬라이싱을 이용하여 수정한다.

s = input()
word = ['U', 'C', 'P', 'C']
arr = []

for w in word:
  if w in s:                              # 만약에 s문자열에 w가 있다면
    arr.append(w)                         # arr 배열에 해당 w 요소를 넣는다.
    s = s[s.find(w)+1:]                   # s의 문자열 범위를 찾은 w 요소의 인덱스 위치의 +1부터 끝까지로 수정해준다.

if ''.join(arr) == 'UCPC':                # arr에 저장된 문자열이 'UCPC'라면
  print('I love UCPC')                    # 'I love UCPC'를 출력

else:
  print('I hate UCPC')                    # 아니라면 'I hate UCPC'를 

  
  
  
  
# 다른 풀이
s = input()

result = ""
for w in "UCPC":
  index = s.find(w)
  if index == -1:                         # s에서 w를 찾지 못하면 더 확인할 필요 없으므로 break
    break
  else:
    result += w
    s = s[index + 1:]

print('I love UCPC' if result == 'UCPC' else 'I hate UCPC')
