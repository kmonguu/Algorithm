// 매개변수로 주어지는 두 수 n, m의 최대공약수와 최대공배수를 출력

// 내가 푼 코드
// n, m 중 작은 값부터 0까지 거꾸로 하나씩 빼면서 각각 n과 m에 나누었을 때 처음으로 나머지가 모두 0이 되는 수를 최대공약수로 구함
// n, m 중 큰 값부터 n*m까지 값을 하나씩 증가시키며 n과 m에 나누었을 때 처음으로 나머지가 모두 0이 되는 수를 최소공배수로 구함

function solution(n, m) {
    var answer = [];
    
    for (let i = Math.min(n, m); i > 0; i--){
        if (n%i==0 && m%i==0){
            answer.push(i);
            break;
        } 
       
    }
    for (let i = Math.max(n, m); i <= (n*m); i++){
        if (i%n==0 && i%m==0){
            answer.push(i);
            break;
        }
    }
    return answer;
}




// 다른 사람 코드
// 유클리드 호제법을 이용한 반복문으로 처리

function gcd(a, b) {                        // 유클리드 호제법을 사용하여 최대공약수를 구함
    while (!!a) [a, b] = [b % a, a];        // !!의 의미는 a의 값을 boolean으로 만들겠다는 의미
    return b;
}

function solution(n, m) {
    const g = gcd(Math.min(n, m), Math.max(n, m));
    return [g, n * m / g];
}
