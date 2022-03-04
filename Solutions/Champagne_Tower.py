class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0] * x for x in range(1, 100 + 2)]

        def pour(row):
            flag = False
            for i in range(len(glasses[row])):
                if glasses[row][i] > 1:
                    glasses[row + 1][i] += (glasses[row][i] - 1) / 2
                    glasses[row + 1][i + 1] += (glasses[row][i] - 1) / 2
                    glasses[row][i] = 1
                    flag = True
            if not flag or (row == query_row):
                return
            else:
                pour(row + 1)

        glasses[0][0] = poured
        pour(0)
        return glasses[query_row][query_glass]


print(Solution().champagneTower(1000000000, 99, 99))
