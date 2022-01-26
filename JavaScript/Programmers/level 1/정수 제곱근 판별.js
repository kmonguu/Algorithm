// 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단할 때
// n이 양의 정수 x의 제곱이라면 x+1의 제곱을 반환, n이 양의 정수 x의 제곱이 아니라면 -1 반환

// 내가 푼 코드
// 양의 정수 n이 제곱 수인지 판별하기 위해 (n**0.5) 값이 1과 나누어떨어지는지 여부를 확인했다. 
// 만약, n이 제곱 수라면 1과 나누었을 때 나머지가 0이 될 것이고, n이 제곱수가 아니라면 (n**0.5)의 값은 소수점이 발생하므로 1과 나누었을 때 나누어떨어지지 않는다.

function solution(n) {
    return (n**0.5) % 1 === 0 ? (parseInt(n**0.5)+1)**2 : -1;
}
