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


// 정수를 문자열로 바꾸는 방법 : tring(x), x.toString(), x + "", `${x}` 
// 문자열을 정수로 바꾸는 방법 : +x, Number(x), parseInt(x)

// 다른 사람 코드

function solution(x) {
    return !(x % (x + "").split("").reduce((sum, cur) => sum + +cur, 0));
}


// spread 문법을 사용한 방법
// x가 12345일 때, x + "" 는 "12345"가 되고,
// ...(x + "")은 "1", "2", "3", "4", "5" 가 된다.
// 현재 코드에서 나온  [...(x + "")]은 ["1", "2", "3", "4", "5"]가 된다.

function solution(x) {
    return !(x % [...(x + "")].reduce((sum, cur) => sum + +cur, 0));
}
