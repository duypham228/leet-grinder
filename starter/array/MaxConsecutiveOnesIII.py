class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = maxLength = 0
        hash = [0, 0]

        for end in range(len(nums)):
            hash[nums[end]] += 1

            while (end - start + 1) - hash[1] > k:
                hash[nums[start]] -= 1
                start += 1

            maxLength = max(maxLength, end - start + 1)

        return maxLength