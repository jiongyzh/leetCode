class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = ''.join(reversed(s))
        result = ''
        max_len = 0
        for i in xrange(len(s)):
            if max_len >= len(s) - i:
                return result
            for j in reversed(xrange(i, len(s))):
                k = len(s) - j -1
                if s[i:j+1] == rs[k:k+j+1-i]:
                    if len(s[i:j+1]) >= max_len:
                        result= s[i:j+1]
                        max_len = len(s[i:j+1])
                    break
        return result

if __name__ == '__main__':
        print Solution().longestPalindrome('aaaabcdcbasss')



