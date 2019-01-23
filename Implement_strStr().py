class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not len(needle):
            return 0
        if len(haystack) < len(needle):
            return -1
        i = 0
        while (len(needle) + i) <= len(haystack):
            if haystack[i:len(needle) + i] == needle:
                return i
            else:
                i += 1
        return -1