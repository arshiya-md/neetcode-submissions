class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l < r:
            sum_ = numbers[l] + numbers[r]

            if sum_ == target:
                return [l+1, r+1] # Adding +1 to indices because problem requires 1-indexed

            if sum_ < target:
                l += 1
            else:
                r -= 1

        