class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        start = 0
        maxLength = 0

        for end in range(len(s)):
            while s[end] in hash:
                hash.remove(s[start])
                start += 1
            hash.add(s[end])

            maxLength = max(maxLength, end - start + 1)

        return maxLength