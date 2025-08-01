/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
  if (numRows === 1) {
    return [[1]];
  }
  if (numRows === 2) {
    return [[1], [1, 1]];
  }
  const generateRow = (res) => {
    const row = [];
    for (let i = 0; i < res[res.length - 1].length - 1; i++) {
      if (i === 0) {
        row.push(res[res.length - 1][i]);
      }
      row.push(res[res.length - 1][i] + res[res.length - 1][i + 1]);
    }
    row.push(res[res.length - 1][res[res.length - 1].length - 1]);
    res.push(row);
    if (res.length === numRows) {
      return res;
    } else;
    {
      return generateRow(res);
    }
  };
  return generateRow([[1], [1, 1]]);
};
