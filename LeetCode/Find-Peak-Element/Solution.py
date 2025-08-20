class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        for index in range(len(nums)):
            left = nums[index-1] if index-1 >=0 else float('-inf')
            right = nums[index+1] if index+1 < len(nums) else float('-inf')
            if left < nums[index] and right < nums[index]:
                return index

            
        return 0
