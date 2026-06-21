class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights) - 1
        
        while l < r:

            area = (r - l) * min(heights[l], heights[r])

            res = max(res,area)

            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
                
        return res
        
# Our aim is to find the container that can hold the maximum amount of water, i.e. the maximum possible area.

# The area of a container is:

# ```
# width × height of the shorter wall
# ```

# Therefore, to maximize the area, we would like both:

# * the width to be as large as possible, and
# * the shorter wall to be as tall as possible.

# Initially, we do not know where tall walls are because we have not inspected any heights yet. The only thing we can be certain about without looking at anything else is the maximum possible width, which is the distance between the first and last walls.

# So we start with the first and last walls and calculate the area:

# ```
# area = (right - left) × min(height[left], height[right])
# ```

# This gives us the best area for the current width. However, we cannot yet conclude that this is the maximum overall area because although every future width will be smaller, there may be taller walls inside that compensate for the loss in width and produce a larger area.

# Therefore, we decrease the width and examine the next possibility.

# Since decreasing the width means moving one of the two walls inward, the question becomes:

# Which wall should we move?

# Suppose the right wall is taller and the left wall is shorter.

# The current area is limited by the shorter left wall.

# Now consider moving the taller right wall inward.

# Two things are guaranteed:

# 1. The width decreases.
# 2. The left wall remains the same, so the height of the shorter wall can never become larger than the current left wall.

# There are two possibilities:

# * The new right wall is taller than the left wall. Then the shorter wall is still the same left wall, while the width has decreased, so the area cannot increase.

# * The new right wall is shorter than the left wall. Then not only has the width decreased, but the shorter wall has become even smaller, so the area again cannot increase.

# Therefore, moving the taller wall can never lead to a better answer.

# The only remaining possibility is to move the shorter wall.

# By moving the shorter wall inward, the width still decreases, but now there is at least a chance of finding a taller wall. If that happens, the increase in the limiting height may outweigh the loss in width and produce a larger area.

# Hence, after calculating the area at each step, we always move away from the shorter wall and continue until the two pointers meet.



