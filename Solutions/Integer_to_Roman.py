class Solution:
    def intToRoman(self, num: int) -> str:
        table = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        res = ''
        divisor = 1000
        while num > 0:
            quot = num // divisor
            if quot == 9:
                res += table[divisor] + table[divisor*10]
            elif quot == 4:
                res += table[divisor] + table[divisor*5]
            else:
                if quot >= 5:
                    res += table[divisor*5]
                    quot -= 5
                res += table[divisor]*quot
            num -= num // divisor * divisor
            divisor //= 10
        return res
num = 3493
print(Solution().intToRoman(num))