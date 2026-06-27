class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Store longest increasing sequence from each idx
        # LIS[0] -> LIS from nums[0], LIS[5] -> LIS from nums[5]
        # Initialize LIS of each idx to 1 bcz from a number min length is 1 (that is itself)
        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
        