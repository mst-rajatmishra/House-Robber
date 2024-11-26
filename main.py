class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: if there are no houses, return 0
        if not nums:
            return 0
        
        # Edge case: if there is only one house, return the amount in it
        if len(nums) == 1:
            return nums[0]
        
        # Initialize dp array
        dp = [0] * len(nums)
        
        # Base cases
        dp[0] = nums[0]  # Only one house, rob it
        dp[1] = max(nums[0], nums[1])  # Two houses, rob the one with more money
        
        # Fill dp array for the remaining houses
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        # The answer is the maximum money robbed from all houses
        return dp[-1]

