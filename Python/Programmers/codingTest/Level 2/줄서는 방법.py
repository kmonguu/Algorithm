
from itertools import permutations

def solution(n, k):
    arr = []
    answer = [num for num in range(1, n+1)]
    
    
    for i in permutations(answer, len(answer)): 
        arr.append(list(i))
        
        if len(arr) >= k:
            break
        
    return arr[-1]
        
