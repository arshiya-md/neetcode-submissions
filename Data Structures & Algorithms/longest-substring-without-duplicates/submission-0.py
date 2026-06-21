class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Don't care to persist substrings, you only need their lenghts
        # There is also no need to store lenghts of all substrings because, we only care about longest
        # If the length is longer than previous stored longest, just replace it with new longest
        longest = 0
        start_idx = 0
        substr = set()
        for end_idx in range(len(s)):
            while s[end_idx] in substr:
                substr.remove(s[start_idx])
                start_idx += 1

            substr.add(s[end_idx])
            longest = max(longest, len(substr))

        return longest
