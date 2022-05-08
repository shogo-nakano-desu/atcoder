import * as fs from "fs";

const input = (fs.readFileSync("/dev/stdin", "utf8") as string).split("\n");

const first = input[0].split(" ").map((a: string) => a);
const H = +first[0];
const W = +first[1];

const second = input[1].split(" ").map((a: string) => a);
const R = +second[0];
const C = +second[1];

const af = (H: number, W: number, R: number, C: number) => {
  if (H === 1 && W === 1 && R === 1 && C === 1) {
    console.log(0);
    return;
  }
  if (H === 1) {
    if (C === 1 || C === W) {
      console.log(1);
      return;
    } else {
      console.log(2);
      return;
    }
  } else if (W === 1) {
    if (R === 1 || R === H) {
      console.log(1);
      return;
    } else {
      console.log(2);
      return;
    }
  } else {
    if (R === 1 || R === H) {
      // 四隅のパターン
      if (C === 1 || C === W) {
        console.log(2);
        return;
      } else {
        console.log(3);
        return;
      }
    } else {
      if (C === 1 || C === W) {
        console.log(3);
        return;
      } else {
        console.log(4);
        return;
      }
    }
  }
};
af(H, W, R, C);
