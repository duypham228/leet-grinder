class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = defaultdict(int)
        matchCount = 0
        for char in s1:
            s1_hash[char] += 1
        
        start = 0
        for end in range(len(s2)):
            if s2[end] in s1_hash:
                s1_hash[s2[end]] -= 1
                if s1_hash[s2[end]] == 0:
                    matchCount += 1
            
            if end - start + 1 > len(s1):
                if s2[start] in s1_hash:
                    if s1_hash[s2[start]] == 0:
                        matchCount -= 1
                    s1_hash[s2[start]] += 1
                start += 1
            
            if matchCount == len(s1_hash):
                return True
        
        return False