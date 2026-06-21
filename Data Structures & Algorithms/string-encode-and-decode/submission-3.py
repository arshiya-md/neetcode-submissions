class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1             
            start = i + 1
            end = start +  int(length)
            res.append(s[start : end])
            i = end
        return res


# curr = 3
# i
# 4#a2#c2#fg#1g#2kl
# 199#a2#c2fg1g2kl
