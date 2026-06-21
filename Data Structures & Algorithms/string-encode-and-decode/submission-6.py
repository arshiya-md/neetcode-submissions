class Solution:

    def encode(self, strs: List[str]) -> str:

        # Commented logic below is inefficient because strings are immutable in CPython.
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
        i  =  0 # Step-1: Initialize i to 0  
        # j = i # Step-9: Do it in while loop
        while i < len(s): # Step-8: Repeat until i reaches end of s

            j = i # Step-10 Initialize j = i here as we need to do this for every iteration
            while s[j] != '#': # Step-2: Keep i fixed, and move j until '#' is reached
                j += 1

            length = int(s[i:j]) # Step-3: Characters from i to j (j excluded) give the length
            start = j+1 # Step-4: Word starts after '#', at index j+1
            end = start + length # Step-5: Compute end index of the word

            # word = s[start:end]
            res.append(s[start:end]) # Step-6: Append the extracted word to result

            i = end # Step-7: Move i to 'end' to decode the next word similarly in next iterations
        
        return res

