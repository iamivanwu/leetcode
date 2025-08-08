/**
 * @param {number} n
 * @return {number}
 */
var soupServings = function (n) {
  if (n > 4800) {
    return 1;
  }
  const f = Math.ceil(n / 25);
  const mapping = Array.from({ length: f + 1 }, () => Array(f + 1).fill(-1));

  const pour = (ra, rb) => {
    if (ra <= 0 && rb > 0) {
      return 1;
    }
    if (ra <= 0 && rb <= 0) {
      return 0.5;
    }
    if (ra > 0 && rb <= 0) {
      return 0;
    }
    if (mapping[ra][rb] !== -1) {
      return mapping[ra][rb];
    }
    mapping[ra][rb] = 0.25 * (pour(ra - 4, rb) + pour(ra - 3, rb - 1) + pour(ra - 2, rb - 2) + pour(ra - 1, rb - 3));
    return mapping[ra][rb];
  };
  return pour(f, f);
};
