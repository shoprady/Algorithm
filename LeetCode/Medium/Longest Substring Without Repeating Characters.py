class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, maxlen, seen = 0, 0, set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            sublen = i - left + 1
            maxlen = max(maxlen, sublen)
            seen.add(s[i])
        return maxlen
