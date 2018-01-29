class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rs = ''
        for n in range(numRows):
            idx = n
            while idx < len(s):
                rs = rs + s[idx]
                idx += 2*(numRows-1)
                if n not in (0, numRows-1):
                    idx1 = idx - 2*n
                    if idx1 < len(s):
                        rs = rs + s[idx1]
        return rs

if __name__ == '__main__':
        print Solution().convert('ABCDE', 4)