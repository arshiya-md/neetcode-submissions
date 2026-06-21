class Solution:
    def climbStairs(self, n: int) -> int:

        # Initialize steps to reach top from 0 to step n with -1
        cache = [-1] * n

        def ways_to_top(from_step):

            # If reached the top(last step - n) or exceeded
            if from_step >= n:
                return  from_step == n # return true if on top step or false if exceeded top

            # If already ways are calculated and stored from current step,
            # No need to recalculate just return the value
            if cache[from_step] != -1:
                return cache[from_step]

            # From the current from_step calculate ways to reach top if taken -
            # One step at a time and two steps at a time
            # Store no.of ways from that step to prevent future re-calculations
            cache[from_step] = ways_to_top(from_step + 1) + ways_to_top(from_step + 2)
            return cache[from_step]

        # start from step 0
        return ways_to_top(0)