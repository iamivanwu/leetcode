/**
 * @param {number[]} basket1
 * @param {number[]} basket2
 * @return {number}
 */
var minCost = function (basket1, basket2) {
  let min = Infinity;
  const parse = (basket) => {
    const b = {};
    for (const item of basket) {
      b[item] = (b[item] ?? 0) + 1;
      min = Math.min(min, item);
    }
    return b;
  };
  const b1 = parse(basket1);
  const b2 = parse(basket2);

  const c = {};
  for (const key of Object.keys(b1)) {
    b2[key] = b2[key] ?? 0;
    const d = Math.abs(b1[key] - b2[key]);
    if (d % 2 === 1) {
      return -1;
    }
    if (d !== 0) {
      c[key] = d;
    }
  }
  for (const key of Object.keys(b2)) {
    b1[key] = b1[key] ?? 0;
    const d = Math.abs(b1[key] - b2[key]);
    if (d % 2 === 1) {
      return -1;
    }
    if (d !== 0) {
      c[key] = d;
    }
  }
  const keys = Object.keys(c);
  let res = 0;
  const arr = [];
  for (const key of keys) {
    let i = 0;
    while (i < c[key] / 2) {
      arr.push(key);
      i += 1;
    }
  }

  for (let i = 0; i < arr.length / 2; i++) {
    res += Math.min(+arr[i], min * 2);
  }

  return res;
};
