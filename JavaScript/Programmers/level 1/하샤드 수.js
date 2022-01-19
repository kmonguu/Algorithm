// 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 한다.
// 예를 들어, 18의 자릿수 합은 1 + 8 = 9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수이다.

// 내가 푼 코드
// for문을 통해 매개변수로 들어오는 양의 정수 x를 문자열로 바꾸고 한 자리씩 int로 answer에 누적합을 구한다.
// 양의 정수 x와 자릿수의 합 answer가 나누어떨어지면 True를 반환, 아니면 False를 반환하도록 한다.

function solution(x) {
    let a = String(x);
    let answer = 0;
    
    for (let i = 0; i < String(x).length; i++){
        answer += parseInt(a[i])
    }
    
    return x % answer == 0;
}
