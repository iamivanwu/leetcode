class Solution:
    def simplifyPath(self, path: str) -> str:
        dist = []
        path = path.replace('//','/')
        content = path.split('/')
        for name in content:
            if name == '.' or name == '':
                continue
            elif name == '..':
                if dist:
                    dist.pop()
            else:
                dist.append(name)
        return '/'.join(dist)