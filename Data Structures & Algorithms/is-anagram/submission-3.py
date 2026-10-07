class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n != m:
            return False

        t_str = ''.join(sorted(t))
        s_str = ''.join(sorted(s))
        if s_str == t_str:
            return True
        else:
            return False
        countS, countT = {}, {}

        for i in range(n):
            countS[s[i]]= 1 + countS.get(s[i], 0)


        for j in range(m):
            countT[t[j]] = 1 + countT.get(t[j], 0)


        return countS == countT
                    