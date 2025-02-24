class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = match = 0
        minLength = float('inf')
        result = [0,0]
        mapT = Counter(t)
        condition = len(mapT)
        
        # extend the right of window
        for end in range(len(s)):
            if s[end] in mapT:
                mapT[s[end]] -= 1
                if mapT[s[end]] == 0:
                    match += 1
                    
            # shrink the left of window
            while match == condition:
                # minLength = min(minLength, end - start + 1)
                if (end - start + 1) < minLength:
                    minLength = end - start + 1
                    result = [start, end]
                if s[start] in mapT:
                    mapT[s[start]] += 1
                    if mapT[s[start]] > 0:
                        match -= 1
                start += 1 
        start, end = result
        return s[start:end+1] if minLength != float('inf') else ""