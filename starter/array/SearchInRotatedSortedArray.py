class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_idx = l

        if min_idx == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[min_idx - 1]:
            l, r = 0, min_idx - 1
        else:
            l, r = min_idx, len(nums) - 1
        
        while l <= r:
            m = (l+r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return -1
        