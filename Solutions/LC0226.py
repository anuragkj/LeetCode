class Solution:
    def minSteps(self, s: str, t: str) -> int:
        lets = [0] * 26
        lett = [0] * 26

        for i in range(len(s)):
            lets[ord(s[i]) - ord('a')] += 1
            lett[ord(t[i]) - ord('a')] += 1
        
        ret = 0
        for i in range(26):
            ret += max(0, lets[i] - lett[i])

        return ret
