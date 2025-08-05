/**
 * @param {number[]} fruits
 * @param {number[]} baskets
 * @return {number}
 */
var numOfUnplacedFruits = function (fruits, baskets) {
  let res = 0;
  for (const f of fruits) {
    let put = false;
    for (let i = 0; i <= baskets.length - 1; i++) {
      if (baskets[i] >= f) {
        baskets[i] = 0;
        put = true;
        break;
      }
    }
    res += put ? 0 : 1;
  }
  return res
};

let fruits = [4, 2, 5],
  baskets = [3, 5, 4];
console.log(numOfUnplacedFruits(fruits, baskets));
