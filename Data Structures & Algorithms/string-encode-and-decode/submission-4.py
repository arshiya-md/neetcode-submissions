class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s))+'#'+s
        return encoded_str

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


