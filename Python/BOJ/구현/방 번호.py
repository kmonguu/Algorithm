# 자기 방의 번호를 플라스틱 숫자로 문에 붙이려고 한다. 플라스틱 숫자 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다.
# 방 번호가 주어졌을 때, 필요한 세트의 최솟값을 출력
# 숫자 6과 9는 뒤집어서 사용할 수 있다.


# 풀이
# 플라스틱 숫자 한 세트만큼 배열을 만들고 0으로 초기화 한다.
# 입력받은 방 번호에 9가 있다면 9를 6으로 바꾸고, 배열의 해당 인덱스에 +1 한다.
# 6과 9는 대체가 가능하므로 한 배열에 같이 카운트하는 것
# 6의 카운트가 저장된 배열의 값을 2로 나눈 몫과 나머지이 합을 구하여 세트의 수를 출력한다.

# 코드
import sys
input = sys.stdin.readline

room_num = input().strip().replace('9', '6')
set = [0]*9

for i in room_num:
  set[int(i)] = room_num.count(i)
set[6] = set[6]//2 + set[6]%2

print(max(set))




# 풀이
# 입력받은 방 번호에 9가 있다면 9를 6으로 바꾼다.
# 플라스틱 세트의 수만큼 배열을 할당하고 방 번호에 6이 있다면 해당 인덱스에 0.5를 더해주고 6이 없다면 1을 더한다.
# 만약 66666와 같이 6이 홀수개로 입력되었다면 소수점 발생하므로 math 모듈을 사용하여 올림해준다.

# 코드
import sys
import math

input = sys.stdin.readline
room_num = input().strip().replace('9', '6')
set = [0]*9

for i in room_num:
  if i == '6':
    set[int(i)] += 0.5
  else:
    set[int(i)] += 1

print(math.ceil(max(set)))
