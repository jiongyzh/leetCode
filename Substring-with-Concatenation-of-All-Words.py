class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        m, n, o, res = len(s), len(words), len(words[0]), []
        if m < n * o:
            return []
        for i in range(m-n*o + 1):
            target = words[:]
            j = i
            while target:
                if s[j:(j+o)] in target:
                    target.remove(s[j:(j+o)])
                    j += o
                else:
                    break
            if not target:
                res.append(i)
        return res

if __name__ == '__main__':
    print Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])