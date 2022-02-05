class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        for i in range(0, len(command)):
            if command[i] == '(':
                continue
            elif command[i] == ')':
                if command[i-1] == '(':
                    res += 'o'
            else:
                res += command[i]
        return res