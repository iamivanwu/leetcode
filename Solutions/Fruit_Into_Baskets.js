/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function (fruits) {
  let res = 0;
  for (let i = 1; i < fruits.length + 1; i++) {
    if (fruits[i] !== fruits[i - 1] || i === fruits.length) {
      let diff = -1;
      let count = 0;
      for (let j = i - 1; j > -1; j--) {
        if (fruits[j] !== fruits[i - 1]) {
          if (diff === -1) {
            diff = fruits[j];
          } else if (fruits[j] !== diff) {
            break;
          }
        }
        count += 1;
      }
      res = Math.max(res, count);
    }
  }
  return res;
};
