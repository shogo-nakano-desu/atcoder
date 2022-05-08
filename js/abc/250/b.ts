import * as fs from "fs";

const input = (fs.readFileSync("/dev/stdin", "utf8") as string).split("\n");

const first = input[0].split(" ").map((a: string) => a);

//ex)N=4,A=3,B=2
const N = +first[0];
const A = +first[1];
const B = +first[2];

//列を作るための関数
//1ブロック分の列を作る
const col = (B: number, bow: "#" | "."): string[] => {
  const r = [];
  for (let i = 0; i < B; i++) {
    r.push(bow);
  }
  return r;
};

//全体の横の列を作る
//sbowには最初の色を入れる
// black = false, white = true
const w = (N: number, sbow: boolean): string[] => {
  const r = [];

  for (let i = 0; i < N; i++) {
    let color: "#" | ".";
    if (i % 2 === 0) {
      color = !sbow ? "#" : ".";
    } else {
      color = sbow ? "#" : ".";
    }
    const one = col(B, color);
    r.push(...one);
  }
  return r;
};

//縦の行を作る
const h = (N: number) => {
  const r = [];
  for (let k = 0; k < N; k++) {
    for (let i = 0; i < A; i++) {
      const col = w(N, k % 2 === 0 ? true : false);
      r.push(col.join(""));
    }
  }
  r.forEach((e) => console.log(e));
};

h(N);
