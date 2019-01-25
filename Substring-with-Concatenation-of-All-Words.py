class Solution(object):
    def findSubstring0(self, s, words):
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
        for i in range(m-n*o+1):
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

    def findSubstring(self, s, words):
        if not words:
            return []
        m, n, o, res = len(s), len(words), len(words[0]), []
        if m < n * o:
            return []
        w_dst = list(set(words))
        w_cnt = list(words.count(x) for x in w_dst)
        w_dic = dict(zip(w_dst, w_cnt))

        for i in range(m-n*o+1):
            target = w_dic.copy()
            j = i
            while j < i + n*o:
                try:
                    if target[s[j:j+o]] > 0:
                        target[s[j:j + o]] -= 1
                        j += o
                    else:
                        break
                except KeyError:
                    break
            if j == i + n*o:
                res.append(i)
        return res


if __name__ == '__main__':
    print Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])