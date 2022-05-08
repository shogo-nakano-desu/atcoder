import * as fs from "fs";

const input = (fs.readFileSync("/dev/stdin", "utf8") as string).split("\n");

const first = input[0].split(" ").map((a: string) => a);

//ex)N=5,Q=5
const N = +first[0];
const Q = +first[1];
const nums: number[] = []; //動かすボール番号
for (let i = 0; i < Q; i++) {
  nums.push(+input[i + 1]);
}

const balls: number[] = [];
for (let i = 0; i < N; i++) {
  balls.push(i + 1);
}

//a,bには対象のインデックスを入れる
const changer = (a: number, b: number): void => {
  const c = balls[a];
  balls[a] = balls[b];
  balls[b] = c;
};

//全体を並び替えていく
for (let i = 0; i < Q; i++) {
  const a = balls.findIndex((e) => e === nums[i]); //動かすボールのインデックス
  let b;
  //右端の時
  if (a === N - 1) {
    b = a - 1;
  } else {
    b = a + 1;
  }
  changer(a, b);
}
console.log(balls.join(" "));
