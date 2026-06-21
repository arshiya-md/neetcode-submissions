class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj_list = defaultdict(list)
        # Forming an adjacency list
        # key -> string pattern, value -> list of words with same pattern
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj_list[pattern].append(word)

        # Find the shortest distance to reach endWord using BFS on the adjacency_list
        q = deque()
        visited = set()
        visited.add(beginWord)
        q.append(beginWord)
        res = 1

        while q:

            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                # Get word's neighbours
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neighbour in adj_list[pattern]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append(neighbour)
            res += 1

        return 0

            



# Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]
# {
#     *at : [cat, bat],
#     c*t : [cat],
#     ca* : [cat],
#     b*t : [bat],
#     ba* : [bat, bag],
#     *ag : [bag, sag, dag],
#     b*g : [bag],
#     s*g : [bag],
#     sa* : [sag],
#     d*g : [dag],
#     da* : [dag],
#     *ot : [dot],
#     d*t : [dot],
#     do* : [dot]
# }

# cat -- bat -- bag -- sag
#                |      |
#               dag------



    