class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = maxLength = maxRepeat = 0
        hash = defaultdict(int)

        for end in range(len(s)):
            hash[s[end]] += 1
            
            while (end - start + 1) - max(hash.values()) > k:
                hash[s[start]] -= 1
                start += 1
            
            maxLength = max(maxLength, end - start + 1)

        return maxLength