class Solution:
    def canJump(self, nums: List[int]) -> bool:

        target = len(nums) - 1

        for i in range (len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                # If target is reachable now check if this current idx is reachable
                # by previous items, so set it ass new target for previous items
                target = i
            # Traverse from back till front to see if target can be reached from any of previosu elements
        
        return target == 0





