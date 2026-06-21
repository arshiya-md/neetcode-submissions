class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        def dfs(i, comb, sum_):
            if sum_ == target:
                res.append(comb.copy())
                return None

            if i >= len(nums) or sum_ > target:
                return None

            comb.append(nums[i])
            dfs(i, comb, sum_ + nums[i])
            comb.pop()
            dfs(i+1, comb, sum_)

        dfs(0,[],0)
        return res
        