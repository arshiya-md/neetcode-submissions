class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        res = []

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        freq_buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)

        for i in range(len(freq_buckets) - 1, 0, -1):
            for n in freq_buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res


