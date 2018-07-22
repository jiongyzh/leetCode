class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s = len(s)
        len_p = len(p)
        if s == p:
            return True
        for i in range(len_p):
            k = i
            for j in range(len_s):
                if s[j] != p[k] and p[k] != '.':
                    break
                k += 1
                if k > len_p -1:
                    return False
                if j == len_s -1:
                    return True
        return False