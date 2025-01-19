class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxLength = end = start = 0
        hash = {}

        for end in range(len(fruits)):
            if fruits[end] not in hash:
                hash[fruits[end]] = 0
            hash[fruits[end]] += 1
            
            while len(hash) > 2:
                hash[fruits[start]] -= 1
                if hash[fruits[start]] == 0:
                    del hash[fruits[start]]
                start += 1

            maxLength = max(maxLength, end - start + 1)

        return maxLength  