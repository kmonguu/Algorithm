// 자연수 n이 매개변수로 주어질 때, n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 수 x를 반환

// 내가 푼 코드

function solution(n) {
    for (let i = 2; i <= n; i++){
        if (n % i == 1) {
            return i;
        }
    }

// 다른 사람 코드
// 나머지가 1이 되도록 하는 가장 작은 수 x를 찾는 범위를 n의 제곱근으로 설정
    
function solution(n) {
    for (let i = parseInt(n ** 0.5); i <= n; i++){
        if (n % i == 1) return i;
    }
}
