# 1번 데이터는 1번 컴퓨터, 2번 데이터는 2번 컴퓨터, 3번 데이터는 3번 컴퓨터, ... ,
# 10번 데이터는 10번 컴퓨터, 11번 데이터는 1번 컴퓨터, 12번 데이터는 2번 컴퓨터, ...

# 총 데이터의 개수는 항상 a^b개의 형태로 주어질 때, 마지막 데이터를 다루는 컴퓨터의 번호를 출력
# 입력받는 a의 일의 자리 수가 마지막 데이터를 다루는 컴퓨터 번호를 좌우한다.

# 총 데이터의 개수가 a의 b제곱이다. 어떠한 수를 제곱하면 1의 자리 수는 반복된다.
# - a의 1의 자리 수를 확인하고 이를 b제곱한 수의 1의 자리 수의 규칙을 파악한다.
# 1일 때 = [1]
# 2일 때 = [2, 4, 8, 6] : 2일 때 n제곱을 하면 일의 자리 수는 2, 4, 6, 8...이 반복된다.
# 3일 때 = [3, 9, 7, 1] : 3일 때 n제곱을 하면 일의 자리 수는 3, 9, 7, 1...이 반복된다.
# 4일 때 = [4, 6]       : 4일 때 n제곱을 하면 일의 자리 수는 4, 6이 반복된다.
# 5일 때 = [5]
# 6일 때 = [6]
# 7일 때 = [7, 9, 3, 1] : 7일 때 n제곱을 하면 일의 자리 수는 7, 9, 3, 1이 반복된다.
# 8일 때 = [8, 4, 2, 6] : 8일 때 n제곱을 하면 일의 자리 수는 8, 4, 2, 6이 반복된다.
# 9일 때 = [9, 1] : 9일 때 n제곱을 하면 일의 자리 수는 9, 1이 반복된다.

# 나머지 1, 5, 6 일 때는 해당 수를 아무리 제곱하더라도 일의 자리가 같다는 것을 알 수 있다.

import sys 
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	a, b = map(int,input().split())
	aRemain=a%10

	if aRemain == 0: # 패턴 1
		print(10)
	elif aRemain in [1,5,6]: 
		print(aRemain)
	elif aRemain in [4,9]: #패턴 2
		bRemain=b%2
		if bRemain == 0:
			print(aRemain*aa%10)
		else:
			print(aRemain)
	else: #패턴 4
		bRemain=b%4  
		if bRemain ==0:
			print(aRemain**4%10)
		else:
			print(aa**bb%10)
