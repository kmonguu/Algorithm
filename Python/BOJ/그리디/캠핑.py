# 캠핑장을 연속하는 P일 중, L일 동안만 사용할 수 있다. 
# 만약 V일짜리 휴가를 보내려고 한다면 캠핑장을 최대 며칠동안 사용할 수 있는지를 출력


# 예제
# P = 20, L = 10, V = 28 일 때, 총 28일의 휴가기간 중 캠핑장을 20일 중 10일만 사용가능하다.
# 캠핑장을 처음 10일 사용하면 그 뒤 10일은 사용 못하고 다시 10일 사용하고 총 휴가기간 동안 캠핑장을 14일 사용할 수 있다.
# oooooooooo xxxxxxxxxx oooooooo 다음과 같이 총 휴가일 중 캠핑장을 사용할 수 있는 날을 체크해보면 총 18일을 사용할 수 있다.


# 풀이
# 식으로 만들어보면 V//P 의 결과로 캠핑장을 P일 동안 꽉채워서 이용할 수 있는 일 수가 된다.
# V%P 의 결과로 남은 휴가일 중 캠핑장을 사용할 수 있는 일 수를 구할 수 있는데, 이때 남은 휴가일이 캠핑장을 이용할 수 있는 날보다 크다면 
# 남은 휴가 기간동안 캠핑장을 사용할 수 있으므로 결과에 더해준다.



# 코드
import sys
input = sys.stdin.readline
count = 0

while True:
  L, P, V = map(int, input().split())

  if L == 0 and P == 0 and V == 0:
    break

  else:
    count += 1
    result = (V // P)*L

    if L < (V % P):
      result += L

    else:
      result += (V % P)

    print('Case %d: %d' %(count, result))

    
    
# 다른 풀이
import sys
input = sys.stdin.readline

index = 0
while True:
  L, P, V = map(int, input().split())
  if L == 0:
    break

  index += 1
  print("Case %d: %d" % (index, (L * (V // P) + min(L, (V % P)))))
