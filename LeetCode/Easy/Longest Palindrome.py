class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        ans = 0

        for ch in s:
            if ch in seen:
                seen.remove(ch)
                ans += 2
            else:
                seen.add(ch)

        return ans + 1 if seen else ans
