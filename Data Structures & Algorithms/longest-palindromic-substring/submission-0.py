class Solution:
    def longestPalindrome(self, s: str) -> str:

        start_idx = 0
        max_len = 0

        for i in range(len(s)):

            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:

                if r - l + 1 > max_len:
                    start_idx = l
                    max_len = r - l + 1

                l = l - 1
                r = r + 1

            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:

                if r - l + 1 > max_len:
                    start_idx = l
                    max_len = r - l + 1

                l = l - 1
                r = r + 1

        return s[start_idx: start_idx + max_len]



        