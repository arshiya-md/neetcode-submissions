class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1

        max_l, max_r = height[l], height[r]
        
        water = 0

        while l < r:

            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                water += max_l - height[l]
            else:
                r -= 1
                max_r = max(height[r], max_r)
                water += max_r - height[r]
            
        return water

# Water trapped at any idx is limited by the shortest height between its maximum left and maximum right
# As we move left pointer towards right we know which is max towards its left because we cross every element to its left to traverse
# Similary, as we move right pointer towards left we know which is max towards its right because we reach here already by traversing the right part
# So at any left pointer idx if you already know its max left and at any right pointer idx you know its right max
# If max right is greater than that of left max thats enough to compute water trapped at that left idx because we dont care if right max gets even bigger it should be just bigger than left max enough 
# because the water trapped is limited by shorter side as mentioned in point 1 
# similarly for right pinter we know right max and when left max is greater than it we know its no use to check for even higher points because it is limited by right max
# so if we are certain at l we compute trapped water at that poisition and if we are certain at r we compute it at r



            
            
        