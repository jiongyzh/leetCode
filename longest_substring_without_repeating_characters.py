class Solution(object):
    def lengthOfLongestSubstring(self, s):
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

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        r, f, i, m = 0, 0, -1, {}
        for v in s:
            i = i+1
            if v in m and m[v] >= f:
                if r < i-f:
                    r = i-f
                f = m[v] + 1
            m[v] = i
        if r < i+1-f:
            r=i+1-f
        return r

    def lengthOfLongestSubstring3(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_val, start, char_dict = 0, 0, dict()
        for i, ch in enumerate(s):
            if ch in char_dict and char_dict[ch] >= start:  # and :
                start = char_dict[ch] + 1
                char_dict[ch] = i
            else:
                char_dict[ch] = i
                val = i - start + 1
                if max_val < val:
                    max_val = val

        return max_val


if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring3('efdgdfavdc')