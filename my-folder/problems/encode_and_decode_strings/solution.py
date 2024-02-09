class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = ""

        for i in strs:
            output += str(len(i))+"#"+i
        
        return output

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        output = []

        i = 0

        while i < len(s): #iterate through each word
            j = i #pointer in the word
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            output.append(s[j+1: j+1+length])

            i = j + length + 1

        return output



        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))