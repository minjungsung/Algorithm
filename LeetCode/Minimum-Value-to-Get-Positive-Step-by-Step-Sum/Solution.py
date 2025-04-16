class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        current=0
        smallest=0
        for num in nums:
            current += num
            smallest = min(smallest, current)

        return 1-smallest