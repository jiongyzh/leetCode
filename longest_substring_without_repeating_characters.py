class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        i, j, max_len = 0, 0, 0
        n = len(s)
        while j < n:
            if s[j] in d:
                i = max(d[s[j]], i)
            d[s[j]] = j + 1
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len


if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring('dvdc')