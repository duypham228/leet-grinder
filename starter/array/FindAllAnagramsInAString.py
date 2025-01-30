class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_hash = defaultdict(int)
        start = matchCount = 0

        result = []
        for char in p:
            p_hash[char] += 1

        for end in range(len(s)):
            if s[end] in p_hash:
                if p_hash[s[end]] == 0:
                    matchCount -= 1
                p_hash[s[end]] -= 1
                if p_hash[s[end]] == 0:
                    matchCount += 1
                # matchCount = sum(1 for value in p_hash.values() if value == 0)
            
            if end - start + 1 > len(p):
                if s[start] in p_hash:
                    if p_hash[s[start]] == 0:
                        matchCount -= 1
                    p_hash[s[start]] += 1
                    if p_hash[s[start]] == 0:
                        matchCount += 1
                    
                start += 1

                # matchCount = sum(1 for value in p_hash.values() if value == 0)

            if matchCount == len(p_hash):
                result.append(start)
        
        return result