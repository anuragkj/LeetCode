class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        c = Counter(s)
        if c['a'] < k or c['b'] < k or c['c'] < k:
            return -1
        n = len(s)
        left = 0
        right = n - 1
        # remove last element so that we can calculate min sliding window which ends on last element
        c[s[-1]] -= 1

        ans = n
        while left <= n:
            c[s[right%n]] += 1
            while c['a'] >= k and c['b'] >= k and c['c'] >= k and left <= n:
                ans = min(ans, right - left + 1)
                c[s[left%n]] -= 1
                left += 1
            right += 1
        return ans
