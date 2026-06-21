class Solution:

    def encode(self, strs: List[str]) -> str:

        # Below logic is inefficient because strings are immutable in CPython.
        # Each concatenation allocates new memory and copies everything built so far.
        # Let 'k' be the average string length.
        # Step 1 copies ~k chars, step 2 copies ~2k, step 3 copies ~3k, and so on.
        # Total copied chars ≈ k(1 + 2 + ... + n) = O(n²)

        # encoded_str = ''
        # for s in strs:
        #     encoded_str += str(len(s))+'#'+s
        # return encoded_str

        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i  =  0
        while i < len(s):

            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            start = j+1
            end = start + length

            word = s[start:end]
            res.append(word)

            i = end
        
        return res
   
# #n3et, ##codecodeco
# 5##n3et12###codecodeco
# traverse till charcter is not # -> 
# the chars till that is len of word ->5


