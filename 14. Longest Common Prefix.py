class Solution():
    def longestPrefix(self, strs: list) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

c1 = Solution()
l1 = ["Dog", "Dogggy","Donte"]

print(c1.longestPrefix(l1))