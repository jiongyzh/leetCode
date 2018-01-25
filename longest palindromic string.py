class Solution(object):
    def longestPalindrome1(self, s):
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

    def longestPalindrome(self, s):
        """
        :param s: str
        :return: str
        """
        start, end = 0, 0
        length_max = 0
        for i in xrange(len(s)):
            if length_max/2 >= len(s) - i:
                return s[start: end + 1]
            len1 = self.expand_from_centre(s, i, i)
            len2 = self.expand_from_centre(s, i, i+1)
            max_len = max(len1,len2)
            if max_len >= length_max:
                start = i - (max_len-1)/2
                end = i + max_len/2
                length_max = max_len
        return s[start: end + 1]


    @staticmethod
    def expand_from_centre(s, left, right):
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left, right = left - 1, right + 1
        return right - left - 1



if __name__ == '__main__':
        print Solution().longestPalindrome('dabcdcbadd')



