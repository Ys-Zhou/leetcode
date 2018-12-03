# 252 / 252 test cases passed.
# Runtime: 55 ms


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path += '/'
        stack = []
        nowstr = ''
        for char in path:
            if char == '/':
                if nowstr == '':
                    pass
                elif nowstr == '.':
                    nowstr = ''
                elif nowstr == '..':
                    if stack:
                        stack.pop()
                    nowstr = ''
                else:
                    stack.append(nowstr)
                    nowstr = ''
            else:
                nowstr += char
        if not stack:
            return '/'
        res = ''
        for name in stack:
            res += '/%s' % name
        return res
