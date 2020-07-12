import re
class Solution:
    month = {
        "Jan": '01',
        "Feb": '02',
        "Mar": '03',
        "Apr": '04',
        "May": '05',
        "Jun": '06',
        "Jul": '07',
        "Aug": '08',
        "Sep": '09',
        "Oct": '10',
        "Nov": '11',
        "Dec": '12'
    }
    def reformatDate(self, date: str) -> str:
        a = date.split(' ')
        b = re.split('[a-z]',a[0])[0]
        if len(b) < 2:
            b = '0' + b
        return a[2] + '-' + self.month.get(a[1]) + '-' + b
    
date = "6th Jun 1933"
print(Solution().reformatDate(date))