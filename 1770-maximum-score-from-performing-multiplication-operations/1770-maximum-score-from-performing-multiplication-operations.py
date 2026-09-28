class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        

        dp = [0] * (m + 1)
        
        for i in range(m - 1, -1, -1):
            next_dp = [0] * (i + 1)
            for left in range(i, -1, -1):
                right = n - 1 - (i - left)
                
                pick_left = multipliers[i] * nums[left] + dp[left + 1]
                
                pick_right = multipliers[i] * nums[right] + dp[left]
                
                next_dp[left] = max(pick_left, pick_right)
            
            dp = next_dp
            
        return dp[0]