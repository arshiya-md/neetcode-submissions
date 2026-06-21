class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        subarr_sum = 0
        subarr_count = 0
        prefix_count = {0 : 1}
        
        for i in range(len(nums)):
            subarr_sum  += nums[i]
            diff = subarr_sum - k

            subarr_count += prefix_count.get(diff, 0)
            prefix_count[subarr_sum] = 1 + prefix_count.get(subarr_sum, 0)

        return subarr_count


        