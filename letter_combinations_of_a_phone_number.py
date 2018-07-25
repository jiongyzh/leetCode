class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitMap = {
            "0": "",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        for d in digits:
            temp = []
            for l in digitMap[d]:
                if len(res):
                    for r in res:
                        temp.append(r + l)
                else:
                    temp.append(l)
            res = temp
        return res


if __name__ == '__main__':
    print Solution().letterCombinations('0129')