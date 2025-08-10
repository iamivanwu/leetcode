/**
 * @param {number} n
 * @return {boolean}
 */
var reorderedPowerOf2 = function (n) {
  let a = 1;
  let arr = [];
  for (let i = 0; i < 30; i++) {
    const count = new Array(10).fill(0);
    for (const c of a.toString()) {
      count[+c] += 1;
    }
    arr.push(count);
    a *= 2;
  }
  const target = new Array(10).fill(0);
  for (const c of n.toString()) {
    target[+c] += 1;
  }
  for (const item of arr) {
    let same = true;
    for (let i = 0; i < 10; i++) {
      if (item[i] !== target[i]) {
        same = false;
        break;
      }
    }
    if (same) {
      return true;
    }
  }

  return false;
};

console.log(reorderedPowerOf2(46));
