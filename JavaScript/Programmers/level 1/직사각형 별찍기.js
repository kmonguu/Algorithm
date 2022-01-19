// 별(*) 문자를 이용하여 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력

// 내가 푼 코드
// a개의 별을 찍는 것을 for문으로 b만큼 반복하도록 하였다.

process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    for (let i = 1; i <= b; i++){
    console.log('*'.repeat(a));
    }
});




// 구조 분해 할당 문법을 사용한 방법

process.stdin.setEncoding('utf8');
process.stdin.on('data', (data) => {
    const [n, m] = data.split(" ");                 // 구조 분해 할당 문법 사용
    
    
    const star = Array(+n).fill("*").join("");      // "+" 사용하여 숫자로 변환하고 Array(+n)으로 n만큼 빈 배열을 만든 뒤, 별표 배열 만들고 join으로 문자열로 변환
    for (let i = 0; i < +m; i++) {
        console.log(star);                          // m만큼 출력
    }
});
