class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)
        n = len(s)

        def dfs(l):
            for r in range(l,n):
                if s[l: r + 1] in word_set:
                    if r + 1 == n:
                        return True
                    if (r + 1) not in visited:
                        visited.add(r + 1)
                        if dfs(r+1):
                            return True
            return False

        visited = {0}
        return dfs(0)
        