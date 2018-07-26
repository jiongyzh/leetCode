class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = []
        dic = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        if not s:
            return True
        for p in s:
            if p in dic:
                temp.append(dic[p])
            else:
                if not temp or temp.pop() != p:
                    return False
        return not temp


if __name__ == '__main__':
    print Solution().isValid('{()[(){}]}')