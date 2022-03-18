// 두 정수 a, b가 주어졌을 때, a와 b 사이에 속한 모든 정수의 합을 반환

// 내가 푼 코드

function solution(a, b) {
    let answer = 0;
    for(let i = Math.min(a, b); i <= Math.max(a, b); i++) {
        answer += i
    }
    return answer;
}

// 다른 사람 풀이 : 두 수 사이의 합을 구하는 공식 사용

function solution(a, b) {
    return (a + b) * (Math.abs(a - b) + 1) / 2;
}
