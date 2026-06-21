class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        t_chars, win_chars = {}, {}

        for c in t:
            t_chars[c] = t_chars.get(c, 0) + 1

        have, need = 0, len(t_chars)
        min_len = float("infinity")
        res = [-1, -1]

        l = 0
        for r in range(len(s)):
            c = s[r]
            win_chars[c] = win_chars.get(c, 0) + 1

            if c in t_chars and win_chars[c] == t_chars[c]:
                have += 1

            while need == have:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    res = [l, r] 

                win_chars[s[l]] -= 1
                if s[l] in t_chars and win_chars[s[l]] < t_chars[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l: r + 1] if min_len != float("infinity") else ""              
