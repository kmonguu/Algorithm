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
