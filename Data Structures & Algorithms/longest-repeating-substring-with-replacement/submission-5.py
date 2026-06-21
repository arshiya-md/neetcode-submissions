class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        freq_map = {}
        
        for r in range(len(s)):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            while (r - l + 1) - max(freq_map.values()) > k:
                freq_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res





        

