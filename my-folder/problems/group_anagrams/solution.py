class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # dict1 = {}
        # output = []
        # for i in strs:
        #     sortedStr = "".join(sorted(i))
        #     if dict1.get(sortedStr) != None:
        #         dict1[sortedStr].append(i)
        #     else:
        #         dict1[sortedStr] = [i]

        # for v in dict1.values():
        #     output.append(v)

        # return output

        dict1 = defaultdict(list)

        for i in strs:
            counts = [0]*26
            for m in i:
                counts[ord(m) - ord("a")] += 1
            
            dict1[tuple(counts)].append(i)

        return dict1.values()


    
        