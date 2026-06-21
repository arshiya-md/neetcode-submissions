class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_len = float('inf')
        subarr_sum = 0
        
        l = 0
        for r in range(len(nums)):
            subarr_sum += nums[r]

            while subarr_sum >= target:
                min_len = min(min_len, r-l+1)
                subarr_sum -= nums[l]
                l += 1

        return min_len if min_len != float('inf') else 0