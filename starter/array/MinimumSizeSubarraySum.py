class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = currSum = 0
        minLength = float('inf')

        for end in range(len(nums)):
            currSum += nums[end]

            while (currSum >= target):
                currLength = end - start + 1

                minLength = min(minLength, currLength)

                currSum -= nums[start]

                start += 1
        
        return 0 if minLength == float('inf') else minLength