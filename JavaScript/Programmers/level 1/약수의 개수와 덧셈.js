// 두 정수 left와 right가 매개변수로 주어졌을 때, left부터 right까지의 모든 수 중에서 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 반환

// 내가 푼 코드
// left와 right사이의 수를 차례대로 순회하며 약수의 개수를 cnt를 증가시키며 구한다.
// 약수의 개수 cnt가 짝수이면 answer배열에 그대로, 홀수개이면 -를 붙여서 배열에 담아준다.
// (약수의 개수가 홀수인 경우는 i가 제곱수인 경우이므로 i의 제곱근의 정수형과 i의 제곱근이 같은지 확인한다.)
// 배열에 담긴 수의 합 reduce를 이용하여 구하면 된다.

function solution(left, right) {
    let answer = []
    for (let i = left; i <= right; i++) {
        parseInt(i**0.5) == i**0.5 ? answer.push(-i) : answer.push(i)
    }
    return answer.reduce((a, b) => a + b, 0);
}
