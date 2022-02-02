// 매개변수로 주어지는 정수 n의 약수를 모두 더한 값을 반환

// 내가 푼 코드

function solution(n) {
    var answer = 0;
    
    for (let num = 1; num <= n; num++){
        if (n % num == 0)
            answer += num;
    }
    return answer;
}
