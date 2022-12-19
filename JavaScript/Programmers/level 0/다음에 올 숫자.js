 // 등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 반환

// 예제
// [1, 2, 3, 4] -> 	5
// 공차가 1인 등차수열이므로 마지막 값 4에 1을 더한 5를 반환

// [2, 4, 8] -> 	16
// 공비가 2인 등비수열이므로 마지막 값 8에 2를 곱한 16을 반환

// 내가 푼 코드 
// 파이썬의 경우 배열의 마지막 요소를 구하기 위한 방법으로 array[-1]을 사용하는데
// 자바스크립트의 경우 안된다..
// common배열의 길이에서 -1뺀 값으로 common배열의 마지막 요소 다음 올 수를 구할 수 있었다.

function solution(common) {
    if (common[1] - common[0] == common[2] -common[1]) {
        return common[common.length-1] + (common[1] - common[0])
    }
    else {
        return common[common.length-1] * (common[1]/common[0])
    }
    
}
