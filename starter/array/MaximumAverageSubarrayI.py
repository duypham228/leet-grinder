class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Sliding Window
        start, end = 0, k - 1
        currSum = sum(nums[:k])
        res = currSum
        while end < len(nums) - 1:
            currSum += nums[end + 1] - nums[start]
            res = max(res, currSum)
            start += 1
            end += 1
        
        return res / k